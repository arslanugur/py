import cv2
_faceCascade = cv2.CascadeClassifier(
  'Cascades/haarcascade_frontalface_default.xml')
_smileCascade = cv2.CascadeClassifier(
  'Cascades/haarcascade_smile.xml')
_camera = cv2.VideoCapture(1)
_camera.set(3,1280)           # length  # 640
_camera.set(4,720)            # height # 480
_fileName = None              # 'smile_recognition.mp4'
_recorder = None
while True:
  _, _square = _camera.read()
  # _square = cv2.flip(_square, -1) # ters gösteriyorsa
  _gray = cv2.cvtColor(_square, cv2.COLOR_BGR2GRAY)
  _faces = _faceCascade.detectMultiScale(
    _gray,
    scaleFactor = 1.2,
    minNeighbors = 5,
    minSize = (30, 30)
  )
  for (x, y, w, h) in _faces:
    cv2.rectangle(_square, (x, y), (x+w,y+h), (255, 0, 0), 2)
    _gray_box = _gray[y:y+h, x:x+w]
    colorful_box = _square[y:y+h, x:x+w]
    _smiles = _smileCascade.detectMultiScale(
      _gray_box,
      scaleFactor = 1.5,
      minNeighbors = 18,
      minSize = (30, 30)
    )
    for (sx, sy, sw, sh) in _smiles:
      cv2.rectangle(colorful_box, (sx, sy), (sx + sw, sy + sh), (0, 0, 225), 2)
      
  cv2.imshow('_square', _square)
  if _recorder is None and _fileName is not None:
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")      # .mp4
    _recorder = cv2.VideoWriter(_fileName, fourcc, 24.0, (_square.shape[1], _square.shape[0], True)
  if _recorder is not None:
    _recorder.write(_square)
    k = cv2.waitKey(10) & 0xff
    if k==27 or k==ord('q'):         # press 'ESC' or 'q' to quit
      break
_camera.release()
if _recorder:
  _recorder.release()
cv2.destroyAllWindows()

                                
                                
