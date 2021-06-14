f = open("live.txt", "wt", encoding="utf-8")
# CP949(EUC-KR) 운영체제의 문자셋으로 처리됨
f.write("""삶이 그대를 속일지라도
믿으라, 기쁨의 날이 오리니""")
f.write("""추가한 내용입니다.""")

f.write("""또 추가합니다.
믿으라, 기쁨의 날이 오리니""")
f.close()

# w는 기존의 것을 버리고 실행
# a는 기존의 것을 냅두고 실행

# 파일 읽기

try:
    f = open('live.txt', 'rt', encoding='utf-8')
    text = f.read()
    print(text)
except FileNotFoundError:
    print('파일이 없습니다.')
finally:
    f.close()
