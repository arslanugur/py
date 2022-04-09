import cv2
import numpy as np
import sys

if sys.platform=='Win32':
  deltax=0
  deltay=0
else:
  deltax=50
  deltay=105
  
camera_ = cv2.VideoCapture(0)
camera_.set(3,640)    # Genişlik
camera_.set(4,400)    # Yükseklik
camera_.set(10, 0.8)  # Parlaklık
while True:
  _, square_ = camera.read()
  ycrcb = cv2.cvtColor(square_, cv2.COLOR_BGR2YCrCb)
  ....
