

### Word Game (a color matching game)
### By Thane Lund, ____________, and Tai Kersten



# Optomization Tasks:
# -Collapse if-else constructions into an array. (Array indexing is faster than if/else constructions)
# -Minimize function calls, create a 'refresh' function (Makes code prettier, fewer functions floating around in NS  )
# -Re-implement the entire thing into an OOP paradigm (Prettier Code, more organized calls, easier to configure without having a dickload of data floating aroound in the header)
#
#

import pygame, random, sys, os, worddata, time, setup
from pygame.locals import *

##########CONFIG########### (Create a seperate .config to edit these constants for User.)
AUTHOR = "Thane Lund"

TITLE = "WORD GAME"

WINDOW_X = 1300 # Set this up in an organic function
WINDOW_Y = 700

FONT = "emulogic.ttf"

FONT_SIZE = 50

SCRAMBLE_SPEED = .05 ## In seconds.  Reduce this number if program is running slow.

WORD_MIN_SIZE = 10
WORD_MAX_SIZE = 300 	

WHITE     =  (255,255,255)
BLACK     =  (  0,  0,  0)
RED       =  (255,  0,  0)
GREEN     =  (  0, 255, 0)
BLUE      =  (  0,   0, 255) 
DARKGREEN =  (  0, 150, 0)
DARKGRAY  =  ( 40, 40, 40)
PINK	=	(250,100,150)


#WORD_BANK = worddata.wordbank
##### /END CONFIG #######

try:
	AUTHOR = setup.AUTHOR
	TITLE = setup.TITLE
	WINDOW_X = setup.WINDOW_X
	WINDOW_Y = setup.WINDOW_Y

	FONT = setup.FONT

	FONT_SIZE = setup.FONT_SIZE

	SCRAMBLE_SPEED = setup.SCRAMBLE_SPEED

	WORD_MIN_SIZE = setup.WORD_MIN_SIZE
	WORD_MAX_SIZE = setup.WORD_MAX_SIZE

	WORD_BANK = setup.WORD_BANK

	WHITE     =  setup.WHITE
	BLACK     =  setup.BLACK
	RED       =  setup.RED
	GREEN     =  setup.GREEN
	BLUE      =  setup.BLUE
	DARKGREEN =  setup.DARKGREEN
	DARKGRAY  =  setup.DARKGRAY
	PINK	=	setup.PINK


	
	
except:
	print "NO Config detected.  Starting with defaults"
	pass




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

class ThaneBit(object):
	
	def __doc__(self):
		"""
		ThaneBit.  v.01
		
		This is the primary game object for the game.  It is called
	ThaneBit because the author of it is unimaginitive.
		
		The game is a word game that cycles through colors and words
	from a word bank situated in setup.py.
		
		It functions by taking 'game' parameters from a setup file 
	determined by the platform administrator.  Then it places them into 
	functions that render, blit, and flip the screen.
	
		So far the parameters taken from the Setup.py are:

			AUTHOR - Author of the game
			TITLE - The title of the game
			WINDOW_X - x-size of window
			WINDOW_Y - y-size of window
			FONT - must be in /bin font str("example.ttf")
			FONT_SIZE - size of font
			SCRAMBLE_SPEED - speed that ctrl+enter cycles
			WORD_MIN_SIZE - Min size of words.  NON FUNCTIONAL
			WORD_MAX_SIZE - Max size of words.  NON FUNCTIONAL
			
			
		CONTROLS:
			CTRL - Does Something
			Z - Does something
			SPACE - Does something else
			
		"""
		
	def __init__(self,
	author = AUTHOR,
	title = TITLE, 
	x = WINDOW_X, 
	y = WINDOW_Y, 
	bgcolor = BGCOLOR, 
	colordict = COLORDICT,
	wordbank = WORD_BANK,
	scramble_speed = SCRAMBLE_SPEED,
	word_min = WORD_MIN_SIZE,
	word_max = WORD_MAX_SIZE,
	font = FONT,
	fontsize = FONT_SIZE
	):
		
		"""
	Takes on the parameters from the setup.py and places them in to the 
	ThaneBit object. 
	"""
		self.author = author
		self.title = title
		self.x_window = x
		self.y_window = y
		self.bgcolor = bgcolor
		self.colordict = colordict
		self.wordbank = wordbank
		self.scramble_speed = scramble_speed
		self.word_min_size = word_min
		self.word_max_size = word_max
		self.fonttype = font
		self.fontsize = fontsize
		
		self.AA = 0
		self.screen = pygame.display.set_mode((self.x_window, self.y_window))
		
		self.story_iterator = worddata.storytime()
		
	###Utility Functions
	
	def __ReturnRandomCoord(self):
		"""
		Retuns a tuple with coordinates for writing words on the screen.
		"""
		
		x = random.randint(1,self.x_window)
		y = random.randint(1,self.y_window)
		return (x,y)

	def __ReturnRandomWord(self):
		"""
		Randomly returns a word from the word bank.
		"""
		
		word_choice = random.randint(0,(len(self.wordbank) -1))
		return self.wordbank[word_choice]


	def __ReturnRandomColorSelect(self):
		"""
		Returns a random color from the color dictionary.  Inactive
	as of this function comment's writing: OCT 2015.
		"""
		
		return self.colordict[random.randint(1,(len(self.colordict)))]


	def __ReturnRandomSize(self):
		"""
		Returns a random integer that is constrained by the user defined
	word max and mins.
		"""
		return random.randint(self.word_min_size, self.word_max_size)

		
	def __ReturnRealRandomColor(self):
		"""
		Returns a random color in range of all available RGB colors.
		"""
		
		red = random.randint(0,255)
		green = random.randint(0,255)
		blue = random.randint(0,255)
		
		return (red, green, blue)


	def __storyTime(self):
		
		"""
		A bunch of silliness.  We don't go there.
		"""
		
		self.background.fill((255,255,255))
		self.__changeText((self.story_iterator.next(),(0,0,0)))
		self.__screenRefresh()
		
	### Background
	
	def __setBackground(self):
		
		"""
		Writes the background surface that gets used for the duration
	of the game loop.
		"""
		
		self.background = pygame.Surface(self.screen.get_size())
		self.backgroundpos = self.background.convert()
		self.backgroundpos = self.background.fill((self.bgcolor))
	
	
	def __changeBackground(self, color_tuple):
		"""
		Changes the background color.
		"""
		
		self.bgcolor = color_tuple
		self.backgroundpos = self.background.fill(self.bgcolor)
	
	### Text: Font
	
	def __setFont(self):
		"""
		Sets the font for the duration of the game loop.
		"""
		
		## Font tuple = (font text, AA, size)
		self.font = pygame.font.Font(self.fonttype, self.fontsize)
	
		self.titlefont = pygame.font.Font(self.fonttype, 20)
	### Text: text
	
	
	def __setText(self):
		
		"""
		Sets initial title screen text.  Also prototype for rewrites.
		"""
		
		self.text = self.font.render(self.title, self.AA, (250,0,250))
		self.textpos = self.text.get_rect()
		self.textpos.centerx = self.background.get_rect().centerx
		self.textpos.centery = self.background.get_rect().centery
		
		
		
		author = "c-circle: %s \n 1986" % self.author
		authortext = self.titlefont.render(author, self.AA, (250,150,150))
		authortextpos = authortext.get_rect()
		authortextpos.centerx = self.background.get_rect().centerx
		authortextpos.y = int(self.y_window*(0.6))
		self.background.blit(authortext,authortextpos) 
		
		del author,authortext,authortextpos
		
		
	def __changeTextPosition(self,coordinate_tuple):
		
		"""
		Changes the position of written texts.
		"""
		
		## coordinate_tuple = (x,y)
		self.background.fill(self.bgcolor)
		self.textpos = self.text.get_rect()
		self.textpos.x = coordinate_tuple[0]
		self.textpos.y = coordinate_tuple[1]
	
	def __changeText(self,(text_string, color_tuple)):
		"""
		Changes the text color.
		"""
		
		self.background.fill(self.bgcolor)
		self.text = self.font.render(text_string,self.AA, color_tuple)
	
	
	###Render/Refresh functions


	def __terminate(self):
		"""
		Exits the program.
		"""
		
		print "Exiting..."
		pygame.quit()
		sys.exit()

		
	
	def __screenRefresh(self):
		"""
		Blits and flips the screen.  Need at the end of each '__change'
	call.
		"""
		
		self.background.blit(self.text,self.textpos)
		self.screen.blit(self.background, self.backgroundpos)
		pygame.display.flip()
		
		
#	def printTest(self,string_test):
#		print string_test
		
	def __displayTitleScreen(self):
		"""
		Generates the title screen.
		"""
	
		
		self.__setBackground()
		self.__setText()
		self.__screenRefresh()
	
	
	def __RandomizeAll(self):
		"""
		Randomly changes the screen, font, and position of text along
		with all their colors.  This is primarily for the screen 
		scramble.
		"""
		
#		print "HELD_TEST"
		self.__changeBackground(self.__ReturnRealRandomColor())
		self.__changeText((self.__ReturnRandomWord(), self.__ReturnRealRandomColor()))
		self.__changeTextPosition(self.__ReturnRandomCoord())
		self.__screenRefresh()
		
		
	def Run(self):
		"""
		Initializes the main game loop.
		"""
		pygame.init()
		print "LOADING GAME..."
		
		self.__setBackground()
		self.__setFont()
		self.__setText()
		self.__screenRefresh()
		
		print "Main Loop initializing"
		
		eventDict = {
		(K_SPACE) : lambda: self.__changeBackground(self.__ReturnRealRandomColor()),
		(K_RETURN) : lambda: self.__changeText((self.__ReturnRandomWord(),self.__ReturnRealRandomColor())),
		(K_z) : lambda: self.__changeTextPosition(self.__ReturnRandomCoord()),
		(K_LCTRL, K_q) : lambda: self.__terminate(),
		(K_SPACE, K_RETURN) : lambda: self.__RandomizeAll(),
		(K_z, K_RETURN) : lambda: self.__storyTime(),
		(K_SPACE, K_z) : lambda: self.__displayTitleScreen(), 
		}  ###How to make this work?
		
		while True:
			for event in pygame.event.get():
				 
#				print event 
				 
				if event.type == KEYDOWN: 
					
					keys = pygame.key.get_pressed()
					
					if event.key in eventDict.keys():
					
						eventDict[event.key]()  ###Tuple comprehension? What is event.key returning?
						self.__screenRefresh()
	
					###Doubles###  ###Figure out how to use DICT, but in the meantime:
					
					if (keys[K_LCTRL] or keys[K_RCTRL]) and keys[K_q]:
						self.__terminate() 
	
					elif keys[K_z] and keys[K_SPACE]:
						self.__displayTitleScreen()
						
					elif keys[K_SPACE] and keys[K_RETURN]:
						
						pressed = True
						
						while pressed == True:
							self.__RandomizeAll()
							
							
							for event in pygame.event.get():
								if event.type == KEYUP:
									pressed = False
	
							time.sleep(self.scramble_speed)
					
					elif keys[K_z] and keys[K_RETURN]:
						self.__storyTime()
					
		#			if event.key == K_SPACE:
		#				print "SPACETEST"
		
		
		
		
		#while True:
		#	for event in pygame.event.get():
		#		if event.type in eventDict.keys():
		#			eventDict[event.key]()
					
		#		else:
		#			pass
					

	'''
	actionDict = {
	K_z : __changeBackground,
	K_RETURN : __changeText,
	K_SPACE : __changeTextPosition,
	(K_Space, K_RETURN) : __RandomizeAll,
	
	
	}
	
	
	'''

x = ThaneBit()
x.Run()
