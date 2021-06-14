import sys

while True:
    ans = input('명령>')
    if ans == 'quit':
        sys.exit(0)       # 종료 상태 0: 정상적인 종료, 1: 메모리 부족, 2:데이터 오류

    print(ans)
