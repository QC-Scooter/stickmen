print("Print background module loading...")
import pygame

screenSize = (1600, 900)
screen = pygame.display.set_mode(screenSize, pygame.RESIZABLE)

def forest():
	screen.fill((0, 204, 255))

def white():
	screen.fill((255, 255, 255))
