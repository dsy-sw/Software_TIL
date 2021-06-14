def calcstep(begin, end, step):
    total = 0
    for num in range(begin, end+1, step):
        total += num

    return total


print('3 ~ 5 =', calcstep(3, 5, 1))
print('3 ~ 5 =', calcstep(begin=3, end=5, step=1))
print('3 ~ 5 =', calcstep(step=1, end=5, begin=3))
print('3 ~ 5 =', calcstep(3, 5, step=1))
print('3 ~ 5 =', calcstep(3, step=1, end=5))

print(1, 2, 3, sep=",", end="======")  # 앞에 123은 포지션 인수, 뒤에 end, sep는 키워드 인수
print(1, 2, 3, end="======", sep=",")
