# Input the path of a directory (ex 'python stitch.py [path-to-dir]')
# Takes all .png files and, in alphabetical order, stitches them together left-to-right.
# Assumes all images are the same size.

import sys
import os
from PIL import Image

print(sys.argv)
path = sys.argv[1]
files = os.listdir(path)
fileCount = len(files)

firstImage = Image.open(path + '/' + files[0])
left = 0
top = 0
bottom = firstImage.height
right = firstImage.width * fileCount
stitchedImage = firstImage.crop((left, top, right, bottom))
for i in range(1, fileCount):
  img = Image.open(path + '/' + files[i])
  stitchedImage.paste(img, (firstImage.width * i, 0))
stitchedImage.save(path + '/' + 'out.png')