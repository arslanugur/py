import cv2

cember = True
square_ = cv2.imread('pictures/money.jpeg')
blur = cv2.GaussianBlur(square_,(3,3),0)
canny = cv2.Canny(blur, 30, 250)
# cv2.imshow("Canny", canny)
# cv2.waitKey(0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
morf_ = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
# cv2.imshow("m_close", m_close)
# cv2.waitKey(0)
_, contours_, _ = cv2.findContours(morf_.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

count_ = 0
for contour in contours:
  alan = cv2.contourArea(contour)
  if alan > 10000:
    # print(alan)
    count_ += 1
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(square_, (x,y), (x + w, y + h), (0, 255, 0), 2)
    if cember:
      (x, y), ycap = cv2.minEnclosingCircle(contour)
      center_ = (int(x), int(y))
      ycap = int(ycap)
      img = cv2.circle(square_, center_, ycap, (255,0,0),2)
if count_ > 0:
  cv2.putText(square_, f"{count_} coin is found", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, 1)

cv2.imshow('square_', square_ )
cv2.waitKey(0)



