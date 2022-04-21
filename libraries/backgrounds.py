print("Background module loading...")
import pygame

screenSize = (1600, 900)
screen = pygame.display.set_mode(screenSize, pygame.RESIZABLE)

def forest():
	screen.fill((23, 195, 255))
	pygame.draw.rect(screen, (0, 153, 51), (0, 700, 1600, 200))
	pygame.draw.rect(screen, (112, 51, 8), (50, 350, 75, 350))
	pygame.draw.rect(screen, (112, 51, 8), (1475, 350, 75, 350))

def white():
	screen.fill((255, 255, 255))
