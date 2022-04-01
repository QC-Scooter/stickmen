import platform
import os
from PIL import Image

print("Sprites module loading...")


#File path designator for stickmen folder
if platform.system() == 'Darwin':
	bonkDoge = Image.open("/Users/msstudent/Documents/GitHub/stickmen/sprites/bonk.jpg")

if platform.system() == 'Windows':
	bonkDoge = Image.open("%appdata%\stickmen\sprites\bonk.jpg")

print("Sprites module loaded")
