# Detect Live Speed of Vehicles

import cv2
import time

cap = cv2.VideoCapture('traffic.mp4')
car_cascade = cv2.CascadeClassifier('cars.xml')
coord = [[637,352], [904,352], [631,512], [952,512]]
dist = 3
while True:
  ret, img = cap.read()
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  cars=car_cascade.detectMultiScale(gray,1.8,2)
  for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
  cv2.line(img, (coord[0][0], coord[0][1]), (coord[1][0], coord[1][1]), (0,0,255),2)
  cv2.line(img, (coord[0][0], coord[0][1]), (coord[2][0], coord[2][1]), (0,0,255),2)
  cv2.line(img, (coord[2][0], coord[2][1]), (coord[3][0], coord[3][1]), (0,0,255),2)  
  cv2.line(img, (coord[1][0], coord[1][1]), (coord[3][0], coord[3][1]), (0,0,255),2)
  for (x, y, w, h) in cars:
    if (x>=coord[0][0] and y==coord[0][1]):
      cv2.line(img, (coord[0][0], coord[0][1]), (coord[1][0], coord[1][1]), (0, 255, 0), 2)
      tim1 = time.time()
      print("Car Entered.")
    if (x>=coord[2][0] and y==coord[2][1]):
      cv2.line(img, (coord[2][0], coord[2][1]), (coord[3][0], coord[3][1]), (0, 255, 0), 2)
      tim2 = time.time()
      print("Car Left.")
      print("Speed in (m/s) is:", dist/((tim1-tim2)))
  cv2.imshow('img', img)
  if cv2.waitKey(20) & 0xFF == ord('q'):
    break
cap.release()    



