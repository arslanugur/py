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
# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV
import cv2

#capture frames from a video
cap  = cv2.VideoCapture('samplecarvideo.mp4')

# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')

# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frames = cap.read()
    
    # convert to gray scale of each frames    
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    
    # Detects cars of different sizes in the input image
    cars = cars_cascade = car_cascade.detectMultiScale(gray, 1.1, 1)
    
    # To draw a rectangle in each cars
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        
    # Display frames in a window
    cv2.imshow('video2', frames)
    
    # Wait for Esc key to stop    
    if cv2.waitKey(33) == 27:
        break

# De-allocate any associated memory usage
cv2.destroyAllwindows()


