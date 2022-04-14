# Nesne Takibi: Kuyruklu Top
import cv2
import imutils
from collections import deque
import numpy as np

fileName = ' ' # 'videos/ab03.mp4'
width = 800       # Genişlik
NOKTA_SAYISI = 100


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
  center_ = None
  if len(contours) > 0:
    cmax = max(contours, key = cv2.contourArea)
    for ctr in contours:
      (x,y), yaricap = cv2.minEnclosingCircle(cmax)
      mts = cv2.moments(cmax):
      center_ = int(mts['m10']/mts['m00']), int(mts['m01']/mts['m00'])
      if yaricap >= 30:
        cv2.circle(square_, (int(x), int(y)), int(yaricap), (255, 255, 0), 4)
      points_.appendleft(center_)
      for i in range(1,len(points_)):
        if points_[i] and points[i-1]:
          # cizgi_kal = int(np.sqrt(NOKTA_SAYISI/float(i+1)) * 1.5) # 5.1
          cizgi_kal=2
          cv2.line(square_,points_[i-1], points_[i], (0,255,255),cizgi_kal)
  cv2.imshow("square_", square_)
  key = cv2.waitKey(10) & 0xFF
  if key == ord('q') or k==27:
    break
camera_.release()
cv2.destroyAllWindows()



