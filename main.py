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

bonkDoge = sprites.bonkDoge

screenSize = (1600, 900)

pygame.init()


screen = pygame.display.set_mode(screenSize, pygame.RESIZABLE)

pygame.display.set_caption("Stickmen v0.1 ALPHA")

done = False

clock = pygame.time.Clock()

clockSpeed = 60


class StickmanFighter(object):
    def __init__(self, data):
        stickman_color = data
        print("Stickman initiated")
        print(stickman_color)

#    def stickSpawn(self):
#


class screenBackground(object):
    def __init__(self, data):
        backgroundImage = data
        print("Background initiated")


red_stickman = StickmanFighter(RED)
blue_stickman = StickmanFighter(BLUE)
bonkDoge.show()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()
            break
