import cv2
import numpy as np

img = cv2.imread('./data/lena.jpg')
wid = 200
hig = 200
pt1 = 0,0
pt2 = wid,hig
cropImage = img[200:200+wid, 400:400+hig]
img[pt1[0]:wid, pt1[1]:hig] = cropImage     # 슬라이싱의 차원 y:x

cv2.rectangle(img, pt1, pt2, (0,255,0),1)
cv2.rectangle(img, (400, 200), (400+wid,200+hig), (0,0,255),1)    # 좌표 (x,y)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()