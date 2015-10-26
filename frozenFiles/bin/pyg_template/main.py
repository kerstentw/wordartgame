

### Word Game (a color matching game)
### By Thane Lund, ____________, and Tai Kersten



# Optomization Tasks:
# -Collapse if-else constructions into an array. (Array indexing is faster than if/else constructions)
# -Minimize function calls, create a 'refresh' function (Makes code prettier, fewer functions floating around in NS  )
# -Re-implement the entire thing into an OOP paradigm (Prettier Code, more organized calls, easier to configure without having a dickload of data floating aroound in the header)
#
#

import pygame, random, sys, os, worddata, time
from pygame.locals import *

##########CONFIG########### (Create a seperate .config to edit these constants for User.)
WINDOW_X = 800 # Set this up in an organic function
WINDOW_Y = 600

SCRAMBLE_SPEED = .05 ## In seconds

WORD_MIN_SIZE = 10
WORD_MAX_SIZE = 300 	

WORD_BANK = worddata.wordbank

WHITE     =  (255,255,255)
BLACK     =  (  0,  0,  0)
RED       =  (255,  0,  0)
GREEN     =  (  0, 255, 0)
BLUE      =  (  0,   0, 255) 
DARKGREEN =  (  0, 150, 0)
DARKGRAY  =  ( 40, 40, 40)
PINK	=	(250,100,150)

COLORDICT = {  ###Use these for randomization
1 : WHITE,
2 : BLACK,
3 : RED,
4 : GREEN,
5 : BLUE,
6 : DARKGREEN,
7 : DARKGRAY,
8 : PINK,
}

BGCOLOR   =  BLUE

##### /END CONFIG #######

###Functions to Randomize stuff

def ReturnRandomWord():
	word_choice = random.randint(0,(len(WORD_BANK) -1))
	return WORD_BANK[word_choice]

def ReturnRandomColor():
	return COLORDICT[random.randint(1,(len(COLORDICT)))]

def ReturnRandomSize():
	return random.randint(WORD_MIN_SIZE, WORD_MAX_SIZE)
	
def ReturnRealRandomColor():
	red = random.randint(0,255)
	green = random.randint(0,255)
	blue = random.randint(0,255)
	
	return (red, green, blue)


def terminate():
	pygame.quit()
	sys.exit()


 ###############
### Main Loop ###
 ###############


def main():

	global FPSCLOCK, DISPLAYSURF, BASICFONT
	mysterious_line = worddata.storytime()
	
	###Title ###//////////FOR OPTOMIZE: Get all this into different functions, using parameters as arguments
										#Better yet, get these into self contained function calls since behavior is finite.
	pygame.init()
	screen = pygame.display.set_mode((WINDOW_X,WINDOW_Y))
	pygame.display.set_caption("Word Game")
	print screen.get_size
	
	wking_background = BGCOLOR #Set this to a variable so when it needs to
								# refresh it can keep colors consistent even
								# when we start randomly changing it.
	
	background = pygame.Surface(screen.get_size())
	backgroundspec = background.convert()
	backgroundspec = background.fill((wking_background))
	
	# font declarations
	font = pygame.font.Font("Courier_New.ttf", 100)
	subfont = pygame.font.Font(None, 25)
	
	# Text definition and positional info
	
	text = font.render("WORD GAME", 0, PINK)
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	textpos.centery = background.get_rect().centery
	
	# Sub-Text definition and positional info
	sub_txt = subfont.render("?? Copyright -- THANE LUND 1983 ??", 0, (0,250,250))
	sub_txt_pos = sub_txt.get_rect()
	sub_txt_pos.y = 500
	sub_txt_pos.x = (WINDOW_X/3)
	
	# Sets the bits in the background surface
	background.blit(text,textpos)
	background.blit(sub_txt, sub_txt_pos) 
	
	###Clear variables.... May need more of this for optomization?
	#del sub_txt_pos, sub_txt, 

	# Sets the 
	screen.blit(background, backgroundspec)
	print pygame.display.flip()
	pygame.display.flip()

	def RandomizeScreen(): ###If this was in a class we could share data without putting a func inside another 
		
		wking_background = ReturnRandomColor()
		backgroundspec = background.fill(wking_background)
		text = font.render(ReturnRandomWord(),0, ReturnRealRandomColor())
		textpos.x = random.randint(0,WINDOW_X-100)	
		textpos.y = random.randint(0,WINDOW_Y-100)
		
		background.blit(text,textpos)
		screen.blit(background, backgroundspec)
		pygame.display.flip()

	  ###########
	###MAIN LOOP###	
	  ###########
	
	while True:
		for event in pygame.event.get():
			print event
			
			if event.type == QUIT:
				return
			
			if event.type == KEYDOWN:
		
				keys = pygame.key.get_pressed()
			
				
				###RAPID COURSE
				
				
				
				if keys[K_q] and (keys[K_RCTRL] or keys[K_LCTRL]):
					terminate()
				
				elif keys[K_z] and keys[K_SPACE]:
					
					wking_background = BGCOLOR 
					
					background = pygame.Surface(screen.get_size())
					backgroundspec = background.convert()
					backgroundspec = background.fill((wking_background))
					
					font = pygame.font.Font("Courier_New.ttf", 100)
					subfont = pygame.font.Font(None, 25)
					
					text = font.render("WORD GAME", 0, PINK)
					textpos = text.get_rect()
					textpos.centerx = background.get_rect().centerx
					textpos.centery = background.get_rect().centery
					
					sub_txt = subfont.render("?? Copyright -- THANE LUND 1983 ??", 0, (0,250,250))
					sub_txt_pos = sub_txt.get_rect()
					sub_txt_pos.y = 500
					sub_txt_pos.x = (WINDOW_X/3)
					
					background.blit(text,textpos)
					background.blit(sub_txt, sub_txt_pos) 
					 
					screen.blit(background, backgroundspec)
					print pygame.display.flip()
					pygame.display.flip()

				
				elif keys[K_RETURN] and keys[K_SPACE]:   ###THIS IS A SHITTY SOLUTION: the second check sucks.  
					go = True
					while go == True:	
						RandomizeScreen()
						time.sleep(SCRAMBLE_SPEED)
						for event in pygame.event.get():
							if event.type == KEYUP:
								go = False
			
				elif keys[K_z] and keys[K_RETURN]:
					go = True
					
					font2 = pygame.font.Font(None, 30)
					
					
					text_long = font2.render(mysterious_line.next(),0,(0,0,0))
			
					textpos2 = text_long.get_rect()
					textpos2.centerx = background.get_rect().centerx
					textpos2.centery = background.get_rect().centery 
					
					
					screen.blit(background, backgroundspec)
					background.blit(text_long, textpos2)
					pygame.display.flip()
					
						
				elif keys[K_RETURN]:
					
					wking_background = ReturnRealRandomColor()
					backgroundspec = background.fill(wking_background)
					
					background.blit(text,textpos)
					screen.blit(background, (0,0))
					pygame.display.flip()
			
				####Changes Words and their color.  
				elif keys[K_z]:#
				
				
					#font = pygame.font.Font(None,ReturnRandomSize())
				
					background2 = background.fill(wking_background)
#					textpos = text.get_rect()
					text = font.render(ReturnRandomWord(), 0, ReturnRandomColor())
					background.blit(text,textpos)
					pygame.display.flip()
			
				###Changes Word Position
				elif keys[K_SPACE]:
					textpos.x = random.randint(0,WINDOW_X-100)	
					textpos.y = random.randint(0,WINDOW_Y-100)
					
					background2 = background.fill(wking_background)
					background.blit(text,textpos)
		
		
			
			screen.blit(background, (0,0))
			pygame.display.flip()




if __name__ == "__main__":
	main()
