import cv2
import sys

cascade_file = "./face/haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_file)

image_file = "./data/face1.jpg"
output_file = "face1-mosaic.jpg"

image = cv2.imread(image_file)
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cascade = cv2.CascadeClassifier(cascade_file)
face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(100,100))

if len(face_list) == 0:
  print("no face")
  quit()

mosaic_rate = 30

print(face_list)
color = (0, 0, 255)

for (x,y,w,h) in face_list:
  face_img = image[y:y+h, x:x+w]
  face_img = cv2.resize(face_img, (w//mosaic_rate, h//mosaic_rate))
  face_img = cv2.resize(face_img, (w,h), interpolation=cv2.INTER_AREA)
  image[y:y+h, x:x+w] = face_img

cv2.imwrite(output_file, image)