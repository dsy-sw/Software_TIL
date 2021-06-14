from audiopi import *
from pydub import AudioSegment
from pydub.playback import play

while True:
  input_str = str(input('입력 : '))
  if input_str == 'quit':
    break

  ret, data = tts(input_str)
  if ret:   # 성공
    sound = io.BytesIO(data.content)
    song = AudioSegment.from_mp3(sound)
    play(song)
  else:   # 실패
    print(data)