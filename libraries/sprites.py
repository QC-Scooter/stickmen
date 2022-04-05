import os
import requests
import pygame

print("Sprites module loading...")

bonkDoge = pygame.image.load(requests.get("https://dogemuchwow.com/wp-content/uploads/2020/12/bonk-it.jpg", stream=True).raw)

print("Sprites module loaded")
