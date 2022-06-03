#!/usr/bin/python3

import glob
import shutil
import os

os.system("mkdir temp")
os.system("rm -f temp/*.jpg")

images =glob.glob("*.jpg")
images.sort()

frame=0
for image in images:
  print(image,"temp/%06d.jpg" %(frame) )

  shutil.copyfile(image,"temp/%06d.jpg" %(frame))
  frame += 1

os.system("ffmpeg -y -r 10 -i temp/%06d.jpg -vf scale=1280:720  out.mp4")
