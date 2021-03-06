#!/usr/bin/python2.7

import pygame
from pygame.locals import *

def main():
	#Initialize Screen
	
	pygame.init()
	screen = pygame.display.set_mode((150,150))
	pygame.display.set_caption("Basic Pygame Program")
	
	#Fill Background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250,250,250))
	
	# Display some text
	
	font = pygame.font.Font(None, 36)
	text = font.render("Hello World", 1, (10,10,10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text,textpos)
	
	# Blit everything to the screen
	screen.blit(background, (0,0))
	pygame.display.flip()
	
	#Event Loop
	while 1:
			for event in pygame.event.get():
				print event.key
				if event.type == QUIT:
					return
					
				screen.blit(background, (0,0))
				pygame.display.flip()
				
if __name__ == "__main__":
	main()
