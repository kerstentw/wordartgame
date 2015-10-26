import pygame, time
from pygame.locals import *


def Create_Status(*args):
	x = 0
	for entries in args:
		print "Note %d : %r" % (x,entries)
		x += 1
def main():




	screen = pygame.display.set_mode((500,500))
	background = pygame.Surface(screen.get_size())


	backgroundstat = background.convert()
	backgroundstat = background.fill((1,1,1))

	screen.blit(background,(0,0))

	
	pygame.init()
	screen  = pygame.display.set_mode((500,500))

	
	def repeater():
		x = 0
		while True:
			print "Hold {} ".format(x)
			x += 1
			pygame.event.get()
			
		
	print pygame.event.get()
	

	while True:
		for event in pygame.event.get():
			
			if event.type == KEYDOWN:
	
				keys = pygame.key.get_pressed()
				#x = 0
				
				#print K_SPACE == True
				
				#if keys[K_SPACE]:
				#	repeater()
					
				if keys[K_SPACE] and keys[K_RCTRL]:
					go = True
					while go == True:	
						print "Wooo"
						time.sleep(.05)
						for event in pygame.event.get():
							if event.type == KEYUP:
								go = False
main()
