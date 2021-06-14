import cv2
import numpy as np

img = np.zeros((512,512,3), dtype=np.uint8)+255

pt1 = 100, 100
pt2 = 400, 400
cv2.rectangle(img, pt1, pt2, (0,255,0),2)     # Green

cv2.line(img, (0,0), (500,0), (255,0,0), 5)   # Blue
cv2.line(img, (0,0), (0,500), (0,0,255), 5)   # Red

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()