import collections
from os import close
import cv2
from tensorflow.python.ops.control_flow_ops import _CheckResults
import net
import json
import numpy as np
from objdetect import ObjDetectApi, NumpyEncoder

PATH_TO_LABELS = 'data/mscoco_label_map.pbtxt'
MODEL_NAME = 'ssd_mobilenet_v1_coco_2017_11_17'

api = ObjDetectApi(MODEL_NAME, PATH_TO_LABELS)

HOST = '127.0.0.1'
PORT = 5000

def filtering(output_dict):
  classes = []
  boxes = []
  scores = []
  for ix, score in enumerate(output_dict['detection_scores']):
    if score > 0.5:
      classes.append(output_dict['detection_classes'][ix])
      boxes.append(output_dict['detection_boxes'][ix])
      scores.append(score)
  return  {
    'detection_classes' : np.array(classes),
    'detection_boxes' : np.array(boxes),
    'detection_scores' : np.array(scores),
  }

def detect(frame):
  frame_rgb = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
  output_dict = api.inference_image(frame_rgb)
  output_dict = filtering(output_dict)
  return output_dict

def receiver(client, addr):
  reader = client.makefile('rb')
  writer = client.makefile('wb')
  while True:
    data, data_len = net.receive(reader)
    if not data :
      if not data: break

    # jpg decode
    data = np.frombuffer(data, dtype=np.uint8)    # byte 배열 -> Numpy 바열
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)   # jpg 이미지 -> BGR이미지

    # object detect
    output_dict = detect(data)

    result = json.dumps(output_dict, cls=NumpyEncoder)
    net.send(writer, result.encode())

  # 이미지 처리
  print('exit receiver')

print('start server...')
net.server(HOST, PORT, receiver)