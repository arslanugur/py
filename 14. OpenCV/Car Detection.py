# pip install opencv-python

# First Code:
import cv2
import numpy as np

cascade_src = 'cars.xml'
# video = 'data/Cars_On_Highway.mp4'
video = 'data/video1.avi'
# video = 'data/video2.avi'

def detectCars(filename):
  rectangles = []
  cascade = cv2.CascadeClassifier(cascade_src)
  
  vc = cv2.VideoCapture(filename)
  
  if vc.isOpened():
    rval , frame = vc.read()
  else:
    rval = false
    
  while rval:
    rval, frame = vc.read()
    frameHeight, frameWidth, fdepth = frame.shape
  
  # Resize
  frame = cv2.resize(frame, (600, 400))
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
  # haar detection
  cars = cascade.detectMultiScale(gray, 1.3, 3)
  
  for (x, y, w, h) in cars:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
  
  # show result
  cv2.imshow("Result",frame)
  
  if cv2.waitKey(33) == ord('q'):
    break
    
vc.release()
detectCars(video)


# Second Code:
import cv2

cap  = cv2.VideoCapture('video.mp4')

car_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    ret, frames = cap.read()
    
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    
    cars = cars_cascade = car_cascade.detectMultiScale(gray, 1.1, 1)
    
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        
    cv2.imshow('video2', frames)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()


