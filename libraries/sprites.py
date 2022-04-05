import platform
import os
from PIL import Image
import requests

print("Sprites module loading...")


bonkDoge = Image.open(requests.get("https://dogemuchwow.com/wp-content/uploads/2020/12/bonk-it.jpg", stream=True).raw)

print("Sprites module loaded")
