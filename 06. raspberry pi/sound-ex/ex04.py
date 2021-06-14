import io, queue
import sounddevice as sd
import soundfile as sf
import sys

samplerate = 44100
channels = 1
sd.default.samplerate = samplerate
sd.default.channels = channels

q = queue.Queue()
recMem = io.BytesIO()

# 녹음 쓰레드 역할
def callback(indata, frames, time, status):
  if status:
    print(status, file = sys.stderr)
  q.put(indata.copy())    # 녹음 데이터 큐에 추가

try:
  with sf.SoundFile(recMem, mode='x', format='wav', samplerate=samplerate, channels=channels) as file:
    with sd.InputStream(callback=callback):
      print('#' * 80)
      print('press Ctrl+C to stop the recording')
      print('#' * 80)
      while True:
        # 큐에 녹음데이터가 있으면 추출하여 파일에 기록
        file.write(q.get())

except KeyboardInterrupt:
  print(recMem.tell())
  # 완료처리
  print('\nRecording finished: ')
except Exception as e:
  print(e)