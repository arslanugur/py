import cv2
import sys
if sys.platform=='win32':
  deltax=0
  deltay=0
else:
  deltax=50
  deltay=105

camera_ = cv.VideoCapture(0)
camera_.set(3,640)
camera_.set(4,480)
while True:
  _, square_ = camera_.read()
  gray_ = cv2.cvtColor(square_, cv2.COLOR_BGR2RAY)
  blur = cv2.GaussianBlur(gray_, (7,7), 0)
  canny = cv2.Canny(blur, 30, 50)
  canny = cv2.bitwise_not(canny)
  # canny = cv2.erode(canny,(7,7),iterations=1)
  # canny = cv2.dilate(canny,(7,7),iterations=1)
  # image_ = cv2.bitwise_and(gray_,gray_, mask=canny)
  image_ = cv2.bitwise_and(square_,square_, mask=canny)
  cv2.imshow("image", image_)
  cv2.moveWindow('image', 10, 10)
  cv2.imshow("canny", canny)
  cv2.moveWindow('canny', image_.shape[1]+deltax,10)
  k = cv2.waitKey(1)
  if k == 27 or k==ord('q'):
    break
    
camera_.release()
cv2.destroyAllWindows()



