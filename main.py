import pygame
import math
import os
import random
import sys
from libraries import stickman_library
from libraries import sprites
from backgrounds import backgrounds
from sounds import sounds
from PIL import Image

BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 0, 255, 0
RED = 255, 0, 0
BLUE = 0, 0, 255

PI = math.pi


screenSize = (1600, 900)

pygame.init()


screen = pygame.display.set_mode(screenSize, pygame.NOFRAME)

pygame.display.set_caption("Stickmen v0.1 ALPHA")

done = False

clock = pygame.time.Clock()

clockSpeed = 20

stickman_height = 85
stickman_width = 15

gravitySpeed = 3

class StickmanFighter(object):
	def __init__(self, data):
		self.stickman_color = data
		if self.stickman_color == "RED":
			self.bodyPosX = 50
			self.bodyPosY = 400
			self.stickman_color = RED
		elif self.stickman_color == "BLUE":
			self.bodyPosX = 1535
			self.bodyPosY = 400
			self.stickman_color = BLUE
		print("Stickman initiated")
		print(self.stickman_color)

	def platformCheck(self):
		if self.bodyPosY == 700 or self.is_on_platform == True:
			self.isJumping = False

	def moveHorizontal(self, direction):
		if direction == 'left':
			self.bodyPosX += -2
		if direction == 'right':
			self.bodyPosX += 2

	def moveVertical(self):
		self.bodyPosY += self.accelerationY

	def jump(self):
		if self.isJumping == True:
			self.isJumping = False
			for self.accelerationY in range(-8, -3, 1):
				self.bodyPosY += self.accelerationY

	def gravity(self):
		if self.bodyPosY < 700:
			self.bodyPosY += gravitySpeed

	def render(self):
		self.renderPosX = self.bodyPosX
		self.renderPosY = self.bodyPosY - stickman_height

		self.feetPosX = self.bodyPosX
		self.feetPosY = self.bodyPosY - 5

		self.feetHitbox = pygame.Rect(self.feetPosX, self.feetPosY, stickman_width, 5)
		self.bodyHitbox = self.renderPosX, self.renderPosY, stickman_width, stickman_height
		pygame.draw.rect(screen, self.stickman_color, self.bodyHitbox)

class screenBackground(object):
	def __init__(self, data):
		self.backgroundImage = data
		if self.backgroundImage == "white":
			backgrounds.white()
		if self.backgroundImage == "BigTree":
			backgrounds.bigTree()


red_stickman = StickmanFighter("RED")
blue_stickman = StickmanFighter("BLUE")

screenBG = screenBackground("white")

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			pygame.quit()
			sys.exit()
			break

	screenBG = screenBackground("white")

	key = pygame.key.get_pressed()

	if key[pygame.K_a]:
		red_stickman.moveHorizontal('left')
	if key[pygame.K_d]:
		red_stickman.moveHorizontal('right')
	if key[pygame.K_w]:
		red_stickman.jump()

	if key[pygame.K_LEFT]:
		blue_stickman.move('left')
	if key[pygame.K_RIGHT]:
		blue_stickman.move('right')
	if key[pygame.K_UP]:
		blue_stickman.jump()

	red_stickman.gravity()
	blue_stickman.gravity()

	red_stickman.render()
	blue_stickman.render()

	pygame.display.flip()
	clock.tick(clockSpeed)
