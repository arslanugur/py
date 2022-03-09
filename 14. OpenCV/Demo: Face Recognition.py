import cv2

faceCascade_ = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
camera_ = cv2.VideoCapture(0)
while True:
  _, square_ = camera_.read()
  # kare = cv2.flip(kare, -1)   # kamera ters gösteriyorsa
  gray_ = cv2.cvtColor(square_, cv2.COLOR_BGR2GRAY)
  faces_ = faceCascade_.detectMultiScale(gray_, scaleFactor = 1.2, minNeighbors = 5, minSize = (20, 20))
  
  for x, y, w, h in faces_:
    cv2.rectangle(square_, (x,y), (x + w, y + h), (255, 0, 0), 2)
  cv2.imshow('kare', square_)
  k = cv2.waitKey(1) & 0xff
  if k == 27 or k == ord('q'):
    break
    
camera_.release()
cv2.destroyAllWindows()


