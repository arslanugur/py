import cv2
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('Cascades/haarcascade_eye.xml)
smileCascade = cv2.CascadeClassifier('Cascades/haarcascade_smile.xml)

camera_ = cv2.VideoCapture(0)
camera_.set(3,1280)          # length
camera_.set(4,720)           # height

fileName_ = None              # 'eye_recognition.mp4'
recorder_ = None

while True:
   ret, square_ = camera_.read()
   # square_ = cv2.flip(square_, -1)    # görüntü ters ise
   gray_ = cv2.cvtColor(square_, cv2.COLOR_BGR2GRAY)
   faces_ = faceCascade.detectMultiScale(gray_, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))
   
   for (x,y,w,h) in faces_:
      # cv2.rectangle(square_, (x,y), (x+w,y+h), (255,0,0), 2)
      # cv2.circle(square_,(int(x+w/2),int(y+h/2)),w//2,(255,0,0),2)
      cv2.ellipse(square_,(int(x+w/2),int(y+h/2)),(w//2,h//2),5,0,360,(255,0,0),2)
      gray_box = gray_[y:y+h, x:x+w]
      colorful_box = square_[y:y+h, x:x+w]
      eyes_ = eyeCascade.detectMultiScale(gray_box, scaleFactor=1.05, minNeighbors=5, minSize=(40,40))

      for (ex, ey, ew, eh) in eyes_:
         # cv2.rectangle(colorful_box, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), cv2.ellipse(colorful_box, (int(ex+ew/2), int(ey+eh/2)), (int(ew/2), int(eh/2)),5,0,360,(0, 255, 0), 2)

      smiles_ = smileCascade.detectMultiScale(gray_box, scaleFactor=1.5, minNeighbors=20, minSize=(60,60))
      for (sx, sy, sw, sh) in smiles_:
         cv.rectangle(colorful_box, (sx, sy), (sx+sw, sy+sh), (0, 0, 255),2)

   cv2.imshow('square_', square_)
   if recorder_ is None and fileName_ is not None:
      fourcc = cv2.VideoWriter_fourcc(*"mp4v")   # .mp4
      recorder_ = cv2.VideoWriter(fileName_, fourcc, 24.0, (square_.shape[1], square.shape[0]), True)
   if recorder_ is not None:
      recorder_.write(square_)
   k = cv2.waitKey(10) & 0xff
   if k == 27 or k == ord('q'):
      break

camera_.release()
if recorder_:
   recorder_.release()
cv2.destroyAllWindows()


