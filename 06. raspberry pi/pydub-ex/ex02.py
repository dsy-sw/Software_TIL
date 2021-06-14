from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_file('converted.mp3', format="mp3")

play(song)