import cv2
import numpy as np

# altRenk = np.array([30, 60, 60])
# ustRenk = np.array([64, 255, 255])
# COLOR = 'green'
# altRenk = (10, 100, 100)
# ustRenk = (40, 255, 255)
# COLOR = 'yellow'
# altRenk = (170, 100, 100)
# ustRenk = (190, 255, 255)
# COLOR = 'red'
altRenk = (75, 100, 100)
ustRenk = (190, 255, 255)
COLOR='blue'
camera_ = cv2.VideoCapture(0)
cember = True
while True:
  if not camera_.isOpened(): break
  _, square_ = camera_.read()
  hsv = cv2.cvtColor(square_, cv2.COLOR_BGR2HSV)
  mask_ = cv2.inRange(hsv, altRenk, ustRenk)
  kernel = np.ones((5,5),'int')
  mask_ = cv2.dilate(mask_,kernel)
  res = cv2.bitwise_and(square_, square_, mask = mask_)
  contours_ = cv2.findContours(mask_.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
  # cv2.drawContours(square_, contours_, -1, (0,255,0),5)
  count_ = 0
  for contour in contours:
    alan = cv2.contourArea(contour)
    if alan > 600:
      count_ += 1
      (x, y, w, h) = cv2.boundingRect(contour)
      cv2.rectangle(square_, (x,y), (x + w, y + h), (0, 255, 0), 2)
      if cember:
        (x, y), ycap = cv2,minEnclosingCircle(contour)
        center_ = (int(x), int(y))
        ycap = int(ycap)
        img = cv2.circle(square_, center_, ycap, (255,0,0),2)
    if count_ > 0:
      cv2.putText(square_, f"{count_} {COLOR} object is found", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 1,1)
      cv2.imshow('square_', square_)
      k=cv2.waitKey(4) & 0xFF
      if k==27: break
if camera_.isOpened():
  camera_.release()
cv2.destroyAllWindows()


