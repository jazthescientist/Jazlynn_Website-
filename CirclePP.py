#!/usr/local/bin/python3
import numpy as np
from PIL import Image, ImageDraw
img = Image.open("images/ProfilePicture.png").convert("RGB")
npImage = np.array(img)
width, height = img.size
diameter = int(min(width, height) * 0.9)  
left = (width - diameter) // 2
top = (height - diameter) // 2
right = left + diameter
bottom = top + diameter
alpha = Image.new('L', img.size, 0)
draw = ImageDraw.Draw(alpha)
draw.ellipse([left, top, right, bottom], fill=255)
npAlpha = np.array(alpha)
npImage = np.dstack((npImage, npAlpha))
Image.fromarray(npImage).save('images/ProfilePicture_Cropped.png')

