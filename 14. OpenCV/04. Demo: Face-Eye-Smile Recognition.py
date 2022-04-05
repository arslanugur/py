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
      cv2.ellipse(square_, ...
