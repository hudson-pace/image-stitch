# Input the path of a directory (ex 'python stitch.py [path-to-dir]')
# Takes all .png files and, in alphabetical order, stitches them together left-to-right.
# Assumes all images are the same size.

import sys
import os
from PIL import Image

# stitch all images in a directory together in one row.
# assumes all images are the same size.
def stitchDir(path):
  files = os.listdir(path)
  fileCount = len(files)
  hasOut = 'out.png' in files
  firstImage = Image.open(path + '/' + files[0]).convert('RGBA')
  left = 0
  top = 0
  bottom = firstImage.height
  right = firstImage.width * (fileCount if not hasOut else fileCount - 1)
  stitchedImage = firstImage.crop((left, top, right, bottom))
  for i in range(1, fileCount):
    if not files[i] == 'out.png':
      img = Image.open(path + '/' + files[i]).convert('RGBA')
      stitchedImage.paste(img, (firstImage.width * i, 0), img)
  stitchedImage.save(path + '/' + 'out.png')

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('USAGE: stitch.py [path-to-dir]')
  else:
    stitchDir(sys.argv[1])