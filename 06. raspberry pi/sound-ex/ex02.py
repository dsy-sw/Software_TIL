import sounddevice as sd
import soundfile as sf

fs = 44100    # Sample rate
seconds = 3   # Duration

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()   # wait until recording is finished

sf.write('output.wav', myrecording, fs)   # Save as WAV file