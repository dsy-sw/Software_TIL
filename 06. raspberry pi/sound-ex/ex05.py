import time
import numpy as np
import sounddevice as sd

duration = 3  # seconds

def print_sound(indata, outdata, frames, time, status):
  volume_norm = np.linalg.norm(indata)*1
  print("|"*int(volume_norm))

with sd.Stream(callback=print_sound):
  sd.sleep(duration * 1000)