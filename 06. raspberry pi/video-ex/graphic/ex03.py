import cv2
import numpy as np

img = np.zeros(shape=(512,512,3), dtype=np.uint8)
cx = img.shape[0] // 2
cy = img.shape[1] // 2

for r in range(100, 300, 100):
  cv2.circle(img, (cx,cy), r, color=(0,0,255), thickness=1)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()