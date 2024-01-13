import stitch
import sys
import os

# Dir of dirs. Run stitch on each dir.
def deepStitch(path):
  dirs = os.listdir(path)
  for dir in dirs:
    stitch.stitchDir(path + '/' + dir)

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('USAGE: stitch.py [path-to-dir]')
  else:
    deepStitch(sys.argv[1])