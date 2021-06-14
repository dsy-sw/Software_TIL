# 사용할 음색 선정
# 무한루프 돌리면서
# 사용자로부터 문자열 입력
# 입력받은 문자열을 음성 합성으로 출력
# quit 입력 시 프로그램 종료

import requests
import io
from pydub import AudioSegment
from pydub.playback import play

URL = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
HEADERS = {
  "Content-Type" : "application/xml",
  "Authorization" : "KakaoAK bc68209ded22c26bb3c2e80894ca0a14"
}

while True:

  data = str(input('입력 :'))
  if data == 'quit': 
    break
  DATA = f"""
  <speak>
  <voice name="WOMAN_READ_CALM">{data}</voice>
  </speak>
  """
# DATA = """
# <speak>
#   그는 그렇게 말했습니다.
#     <voice name="MAN_DIALOG_BRIGHT">잘 지냈어? 나도 잘 지냈어.</voice>
#     <voice name="MAN_READ_CALM">응.</voice>
#     <voice name="WOMAN_READ_CALM">응.</voice>

#     <voice name="WOMAN_DIALOG_BRIGHT" speechStyle="SS_ALT_FAST_1">금요일이 좋아요.</voice>
#     </speak>
#     """

  res = requests.post(URL, headers = HEADERS, data = DATA.encode('utf-8'))

  if res.status_code == 200:  # 성공

    sound = io.BytesIO(res.content)
    song = AudioSegment.from_mp3(sound)

    play(song)

  else: # 실패
    print(res.status_code)
    print(res.json())