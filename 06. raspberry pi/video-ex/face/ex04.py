import cv2
import numpy as np
import time

face_classifier = cv2.CascadeClassifier('./face/haarcascade_fullbody.xml')

cap = cv2.VideoCapture('./data/vtest.avi')       # n번 카메라

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size : ', frame_size)

if cap.isOpened():
  print('width: {}, height : {}'.format(cap.get(3), cap.get(4)))
else:
  print("No Camera")

while True:
  start_time = time.time()
  ret, frame = cap.read()
  if ret:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cropped_face=None
    
    bodys = face_classifier.detectMultiScale(gray, 1.3, 5, minSize=(10,10))
    for (x,y,w,h) in bodys:
      cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 3)

    cv2.imshow('video', frame)

    if cv2.waitKey(1) == 27: break
  else:
    print('video end')
    break

cap.release()
cv2.destroyAllWindows()