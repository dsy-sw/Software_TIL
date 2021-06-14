import sounddevice as sd
import soundfile as sf
from gpiozero import Button, LED
from audioapi import *
from signal import pause

fs = 44100    # Sample rate
seconds = 3   # Duration
duration = 5.5

led = LED(20)
btn = Button(21)

def start_record():
  led.on()
  myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
  sd.wait()   # wait until recording is finished
  sf.write('output.wav', myrecording, fs)   # Save as WAV file

  with open('ouput.wav', 'rb') as f:
    audio = f.read()
    ret, data = stt(audio)
    if ret:
      print('인식 결과', data)
    else:
      print('인식 실패', data)
  led.off()

btn.when_pressed = start_record

pause()