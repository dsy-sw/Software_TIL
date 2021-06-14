# 화소 접근 : 그레이스케일 영상
import cv2
import numpy as np

img = cv2.imread('./data/lena.jpg')
img[120,200] = 0
print(img[100:110, 200:210])

img[400:500, 300:400]

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()