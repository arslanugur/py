import cv2
import numpy as np

square_ = cv2.imread('pictures/money.jpeg')
cember = True
blur = cv2.GaussianBlur(square_,(11,11),0)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
# cv2.waitKey(0)
_, sb = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Gürültü Temizliği
kernel = np.ones((3,3), np.uint8)
sb = cv2.morphologyEx(sb, cv2.MORPH_OPEN, kernel, iterations=3)
sb = cv2.morphologyEx(sb, cv2.MORPH_CLOSE, kernel)
cv2.imshow('sb',sb)
# cv2.waitKey(0)

kenar_ = cv2.Canny(sb, 10, 50)
_, contours_, _ = cv2.findContours(kenar_.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

count_ = 0
for contour in contours:
  alan = cv2.contourArea(contour)
  if alan > 1000:
    print(alan)
    count_ += 1
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(square_, (x,y), (x + w, y + h), (0, 255, 0), 2)
    if cember:
      (x, y), ycap = cv2,minEnclosingCircle(contour)
      center_ = (int(x), int(y))
      ycap = int(ycap)
      img = cv2.circle(square_, center_, ycap, (255,0,0),2)
if count_ > 0:
  cv2.putText(square_, f"{count_} coin is found", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, 1)

cv2.imshow('square_', square_ )
k=cv2.waitKey(0)\
cv2.destroyAllWindows()


