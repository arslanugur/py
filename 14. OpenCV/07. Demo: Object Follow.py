# Following the ball
import cv2
import imutils
import sys

if sys.platform=='win32':
  deltax=0
  deltay=0
else:
  deltax=50
  deltay=105
video_file = ' '   # 'videos/ab03.mp4'
width = 600       # Genişlik
sadece_max = False
green = ((29, 86, 6), (64, 255, 255))
red = ((139, 0, 0), (255, 160, 122))
blue = ((110, 50, 50), (130, 255, 255))
orange = ((160, 100, 47), (179, 255, 255))
yellow = ((10, 100, 100),(40, 255, 255))

altrenk, ustrenk = blue
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
  
