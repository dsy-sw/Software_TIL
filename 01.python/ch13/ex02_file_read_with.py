# 파일 처리시에는 with를 많이쓴다.
# 반드시 close해야하는 상황일때 with를 쓴다.

try:
    # f = open('liveㅌ.txt', 'rt')
    with open('live.txt', 'rt') as f:
        text = f.read()  # 예외 발생시 with 블럭을 벗어날때 close() 자동 호출됨
        print(text)
except Exception as e:
    print('예외발생', e)
    # print('파일이 없습니다.')
# finally:
#     if f:
#         f.close()