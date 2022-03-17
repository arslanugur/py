import cv2

faceCascade_ = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_deafault.xml')
eyeCascade_ = cv2.CascadeClassifier('Cascades/haarcascade_eye.xml')

camera_ = cv2.VideoCapture(0)
camera_.set(3, 1280)          # Genişlik
camera_.set(4, 720)           # YÜkseklik
fileName_ = None              # 'göz_saptama.mp4'
recorder_ = None

while True:
  _, square_ = camera_.read()
  # square_ = cv2.resize(square_, 1280, 720)
  # square_ = cv2.flip(square_, -1)
  gray_ = cv2.cvtColor(square_, cv2.COLOR_BGR2GRAY)
  faces_ = faceCascade_.detectMultiScale(gray_, scaleFactor = 1.2, minNeighbors = 5, minSize = (20, 20))
  
  for (x, y, w, h) in faces_:
    cv2.rectangle(square_, (x, y), (x + w, y + h)), (255, 0, 0), 2)
    gray_box = gray_(y:y+h, x:x+w)
    colorful_box = square_(y:y+h, x:x+w)
    eyes_ = eyeCascade.detectMultiScale(gray_box, scaleFactor = 1.5, minNeighbors = 10, minSize = (3, 3))
    for (ex, ey, ew, eh) in eyes:
      cv2.rectangle(colorful_box, (ex, ey), (ex + ew + ey + eh), (0, 255, 0), 2)
  cv2.imshow('square_', square_)
  if recorder_ is None and filename_ is not None:
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")    # .mp4
    recorder_ = cv2.VideoWriter(fileName_, fourcc, 24.0, (square_.shape[1], square_.shape[0]), True)
  
  if recorder_ is not None:
    recorder_.write(square_)
  k = cv2.waitKey(10) & 0xff
  
  if k == 27 or k == ord('q'):  # press 'ESC' or 'q' to quit 
    break
    
camera_.release()
if recorder_:
  recorder_.release()
cv2.destroyAllWindows()


