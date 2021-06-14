import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg')

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)      # 색상보다 윤곽선 정보가 중요할 때, ***사용빈도 높음
yCrCv = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)        # 다른 라이브러리 연동 시, ***사용빈도 높음

cv2.imshow('gray', gray)
cv2.imshow('yCrCv', yCrCv)
cv2.imshow('hsv', hsv)
cv2.imshow('rgb', rgb)

cv2.waitKey()
cv2.destroyAllWindows()