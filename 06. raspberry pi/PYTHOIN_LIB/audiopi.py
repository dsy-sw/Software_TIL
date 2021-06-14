# 음성 인식/합성을 위한 helper 함수

# 음성 합성 함수명 tts()
#   매개변수 : 합성할 문자열, 음색(디폴트 값 지정)
#   반환값 : 성공여부, mp3데이터(실패 시 에러 원인)

# 음성 인식 함수 명 stt()
#   매개변수 : 음성 데이터(ByteIO 객체)
#   반환값 : 성공여부, 인식 문자열

import json
import requests
import io

rest_api_key = 'bc68209ded22c26bb3c2e80894ca0a14'


def tts(input_str, voice='MAN_DIALOG_BRIGHT'):
  TTS_URL = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
  TTS_HEADERS = {
    "Content-Type" : "application/xml",
    "Authorization" : "KakaoAK " + rest_api_key
  }

  data = f'<speak><voice name={voice}>{input_str}</voice></speak>'
  res = requests.post(TTS_URL, headers = TTS_HEADERS, data = data.encode('utf-8'))

  if res.status_code == 200:  # 성공
    return True, res.content
  else: # 실패
    return False, res.json()

def stt(audio):
  STT_URL = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
  STT_HEADERS = {
    "Content-Type" : "application/octet-stream",
    "X-DSS-Service" : "DICTATION",
    "Authorization" : "KakaoAK "+ rest_api_key
  }

  res = requests.post(STT_URL, headers = STT_HEADERS, data = audio)
  if res.status_code == 200:  # 성공
    result_json_string = res.text[
      res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1
    ]
    result = json.loads(result_json_string)
    return True, result['value']
  else: # 실패
    return False, res.json()