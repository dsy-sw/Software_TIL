total = 0
for num in range(1, 101):
    total += num

print('total =', total)

total = 0
for num in range(2, 101, 2):
    total += num

print('total =', total)

for a in range(5):
    print('이 문장을 반복합니다.')

for x in range(1, 51):
    if (x % 10) == 0:
        print('+', end='')
    else:
        print('-', end='')

# 위에꺼랑 같은거

for x in range(5):
    print('-'*9, end='')
    print('+', end='')