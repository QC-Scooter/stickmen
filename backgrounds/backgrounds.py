print("Background module loading...")
import pygame

BLACK = (0, 0, 0)

screenSize = (1600, 900)
screen = pygame.display.set_mode(screenSize, pygame.NOFRAME)


def bigTree():
	bigTreeFile = pygame.image.load(r"backgrounds/BigTree.png")
	screen.blit(bigTreeFile, (0, 0))

def white():
	screen.fill((255, 255, 255))
	pygame.draw.rect(screen, BLACK, (0, 700, 1600, 200))
