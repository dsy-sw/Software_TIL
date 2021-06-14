from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_file('output.wav', format="wav")

play(song)      # 동기함수(play가 끝나고 다음으로 넘어감)
print('exit')