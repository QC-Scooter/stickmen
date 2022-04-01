import platform
import os
from PIL import Image

def __init__():
	print("Sprites module loading...")

	#File path designator for stickmen folder
	if platform.system() == 'Darwin':
		bonkDoge = Image.open("~/Documents/GitHub/stickmen/sprites/bonk.jpg")

	if platform.system() == 'Windows':
		bonkDoge = Image.open("%appdata%\stickmen\sprites\bonk.jpg")

	print("Sprites module loaded")
