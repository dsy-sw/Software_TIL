str = '89점'
try:
    score = int(str)
    print(score)
except:
    print('예외가 발생했습니다.')

print('작업완료')

# 예외가 발생했습니다.
# 작업완료


while True:
    str = input('점수를 입력하세요 : ')
    try:
        score = int(str)
        print('입력한 점수 :', score)
        break
    except:
        print('점수 형식이 잘못되었습니다.')
print('작업완료')

# 점수를 입력하세요 : 만점
# 점수 형식이 잘못되었습니다.
# 점수를 입력하세요 : 99
# 입력한 점수 : 99
# 작업완료