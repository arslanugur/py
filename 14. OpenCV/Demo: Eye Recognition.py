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
  
