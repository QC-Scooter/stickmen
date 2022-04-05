import pygame
import math
import os
import random
import sys
from libraries import stickman_library
from libraries import sprites
from PIL import Image

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PI = math.pi


screenSize = (1600, 900)

pygame.init()


screen = pygame.display.set_mode(screenSize, pygame.RESIZABLE)

pygame.display.set_caption("Stickmen v0.1 ALPHA")

done = False

clock = pygame.time.Clock()

clockSpeed = 60


stickman_height = 85
stickman_width = 15

class StickmanFighter(object):
	def __init__(self, data):
		self.stickman_color = data
		if self.stickman_color == (255, 0, 0):
			self.posX = 50
			self.posY = 1660
		elif self.stickman_color == (0, 0, 255):
			self.posX = 250
			self.posX = 1660
		print("Stickman initiated")
		print(self.stickman_color)

	def stickSpawn(self):
		self.bodyHitbox = pygame.Rect(self.posX, self.posY, stickman_width, stickman_height)
		pygame.draw.rect(screen, self.stickman_color, self.bodyHitbox)

class screenBackground(object):
    def __init__(self, data):
        backgroundImage = data
        print("Background initiated")


red_stickman = StickmanFighter(RED)
blue_stickman = StickmanFighter(BLUE)

red_stickman.stickSpawn()
blue_stickman.stickSpawn()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			pygame.quit()
			sys.exit()
			break

		bonkDoge = sprites.bonkDoge

		pygame.display.flip()
