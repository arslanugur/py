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
camera_.set(3,640)    # Width
camera_.set(4,400)    # Height
camera_.set(10, 0.8)  # Brightness
while True:
  _, square_ = camera.read()
  ycrcb = cv2.cvtColor(square_, cv2.COLOR_BGR2YCrCb)
  ycrcb = cv2.inRange(ycrcb, (0, 137, 85), (255, 180, 135))
  ycrcb = cv2.morphologyEx(ycrcb, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
  ycrcb = cv2.dilate(ycrcb, (11, 11), iterations=1)
  ycrcb = cv2.erode(ycrcb, (11,11), iterations=1)
  ycrcb = cv2.medianBlur(ycrcb, 5)
  result_ = cv2.bitwise_and(square_, square_, mask=ycrcb)
  cv2.imshow("square_",square_)
  cv2.imshow("mask",ycrcb)
  cv2.imshow("result_",result_)
  cv2.moveWindow('square_', 10, 10)
  cv2.moveWindow('mask',10, square_.shape[0]+deltay)
  cv2.moveWindow('result_', square_.shape[1]+deltax, square_.shape[0]+deltay)
  k = cv2.waitKey(10)
  if k==27 or k==ord('q'):
    break
    
camera_.release()
cv2.destroyAllWindows()




