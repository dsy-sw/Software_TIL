# 1에서 100까지의 수에서

# 짝수의 합 : XXXX
# 홀수의 합 : yyyy

num = 1
xxxx = 0
yyyy = 0

# While 루프로 합계구하기
while num <= 100:
    # num이 짝수인지 홀수인지 판단.
    if num % 2 == 0:  # 짝수이면
        xxxx += num
    else:  # 홀수이면
        yyyy += num
    num += 1

print('짝수의 합 =', xxxx)
print('홀수의 합 =', yyyy)

while True:  # 무한 루프
    print('Hello world')
    ch = input('입력')
    if ch == 'Exit':
        break
