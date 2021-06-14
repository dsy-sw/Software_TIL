from picamera import PiCamera
from time import sleep

camera = PiCamera()

# 180도 회전
# camera.rotation = 180

camera.start_preview()    # 미리보기
# camera.start_preview(alhpa=200)   # 투명도 설정

sleep(10)

camera.stop_preview()