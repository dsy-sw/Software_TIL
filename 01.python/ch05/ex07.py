# 문제

# 컴퓨터와 가위바위보를 해서 승자 판정
# 컴퓨터는 랜덤하게 결정
# 사용자는 input으로 값 입력

# 1. 정보의 표현방법 결정
# 가위 : 1
# 바위 : 2
# 보 : 3

# 2. [1, 2, 3] 중에서 랜덤하게 숫자 하나 결정
import random  # 모듈 --- 함수의 그룹/파일
# random.py 파일을 ex03.py안으로 가져오겠다.

SCISSORS = 1
ROCK = 2
PAPER = 3

com = random.randrange(1, 4)  # [1..4) 4는 포함 X 컴퓨터 값 결정

# 3. 사용자의 값 결정
user = int(input('가위(1),바위(2),보(3):'))

# 4. 승부 판정
if com == user:
    print('무승부', 'com=', com, 'user=', user)
elif user == SCISSORS and com == PAPER:
    print('user 승', 'com=', com, 'user=', user)
elif user == ROCK and com == SCISSORS:
    print('user 승', 'com=', com, 'user=', user)
elif user == PAPER and com == ROCK:
    print('user 승', 'com=', com, 'user=', user)
else:
    print('com 승', 'com=', com, 'user=', user)
