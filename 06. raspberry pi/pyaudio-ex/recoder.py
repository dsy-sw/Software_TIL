import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

RECORD_SECONDS = 5
WAVE_OUPPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()
stream = p.open(input_device_index=1,
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Start to record the audio")
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
  data = stream.read(CHUNK, exception_on_overflow=False)
  frames.append(data)

print("Recording is finished")

stream.stop_stream()
stream.close()
p.terminate()

# wav 파일 저장
wf = wave.open(WAVE_OUPPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()