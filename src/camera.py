#!/usr/bin/env python
# MIT License
# Kevin Walchko 2018

from __future__ import print_function
from __future__ import division
from picamera import PiCamera
from time import sleep

import sys
if sys.platform not in ['linux', 'linux2']:
  raise Exception('You can only run this on a Raspberry Pi with linux')

# camera max resolution:
#   still: 2592 x 1944 px
#   video: 1920 x 1080 px

if __name__ == "__main__":
  camera = PiCamera()
  camera.resolution = (2592, 1944)
  camera.framerate = 3
  
  while True:
    try:
      camera.capture('still.jpg')
      sleep(1)
    except Exception as e:
      print(e)
      break
