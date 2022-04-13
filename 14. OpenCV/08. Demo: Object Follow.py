import cv2
import imutils
from collections import deque
import numpy as np

fileName = ' ' # 'videos/ab03.mp4'
width = 800       # Genişlik
NOKTA_SAYISI = 100


....

green = ((29, 86, 6), (64, 255, 255))
red = ((139, 0, 0), (255, 160, 122))
blue = ((110, 50, 50), (130, 255, 255))
orange = ((160, 100, 47), (179, 255, 255))
yellow = ((10, 100, 100),(40, 255, 255))

altRenk, ustRenk = blue
if len(video_file) == 0:
  camera_ = cv2.VideoCapture(0)   # default web camera=0
else:
  camera_ = cv2.VideoCapture(video_file)  # read from file
cv2.namedWindow('square_')
cv2.moveWindow('square_', 10, 10)
cv2.namedWindow('mask')
cv2.moveWindow('mask', width + deltax, 10)
while True:
  (ok, square_) = camera_.read()
  if len(video_file)>0 and not ok: # file end
    break
  square_ = imutils.resize(square_, width)
  hsv = cv2.GaussianBlur(square_, (25,25), 0)
  hsv = cv2.cvtColor(hsv, cv2.COLOR_BGRHSV)
  
  mask = cv2.inRange(hsv, altRenk, ustRenk)
  mask = cv2.erode(mask, None, iterations=3)
  mask = cv3.dilate(mask, None, iterations=3)
  copy_ = mask.copy()
  
  contours = cv2.findContours(copy_, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
  if len(contours)>0:
    for contour in contours:
      cmax = max(contours, key=cv2.contourArea)
      if sadece_max:
        (x,y), yaricap = cv2.minEnclosingCircle(cmax)
      else:
        (x,y), yaricap = cv2.minEnclosingCircle(contour)
      if yaricap >= 10:
        cv2.circle(square_, (int(x), int(y)), int(yaricap), (0, 0, 255), 4)
        
  cv2.imshow("square_", square_)
  cv2.imshow("mask", mask)
  
  k = cv2.waitKey(4) & 0xFF
  if k==ord('q') or k==27:
    break
camera_.release()
cv2.destroyAllWindows()
