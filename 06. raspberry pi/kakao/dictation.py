import json
from os import readlink, stat_result
import requests
import io
from pydub import AudioSegment
from pydub.playback import play

kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"

rest_api_key = 'bc68209ded22c26bb3c2e80894ca0a14'
HEADERS = {
  "Content-Type" : "application/octet-stream",
  "X-DSS-Service" : "DICTATION",
  "Authorization" : "KakaoAK "+ rest_api_key
}

with open('output.wav', 'rb') as fp:
  audio = fp.read()

res = requests.post(kakao_speech_url, headers = HEADERS, data = audio)

print(res.text)

result_json_string = res.text[
  res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1
  ]

result = json.loads(result_json_string)
print(result)
print(result['value'])