import pyaudio
import wave
import sys

CHUNK = 1024
WAVE_FILENAME = "output.wav"
wf = wave.open(WAVE_FILENAME, 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
channels = wf.getnchannels(),
rate = wf.getframerate(),
output=True)

data = wf.readframes(CHUNK)

while data:
  stream.write(data)
  data = wf.readframes(CHUNK)
  
stream.stop_stream()
stream.close()

p.terminate()