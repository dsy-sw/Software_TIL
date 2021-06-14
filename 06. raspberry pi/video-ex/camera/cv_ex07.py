import cv2

# cap = cv2.VideoCapture(0)       # n번 카메라
# cap = cv2.VideoCapture('./data/vtest.avi')       # n번 카메라
cap = cv2.VideoCapture('http://127.0.0.1:8000/mjpeg/stream')    # ip카메라

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size : ', frame_size)

while True:
  retval, frame = cap.read()    # 프레임 캡쳐
  if not retval: break

  cv2.imshow('frame', frame)
  key = cv2.waitKey(25)       # 1000/25 = 최대 40fps
  if key == 27:break          # esc 키를 누르면 종료
if cap.isOpened():
  cap.release()

cv2.destroyAllWindows()