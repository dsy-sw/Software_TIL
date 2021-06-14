def calcstep(begin, end=1, step=1):  # 디폴트값은 뒤로 다 몰아야 한다.
    total = 0
    for num in range(begin, end+1, step):
        total += num
    return total


print('1~10 =', calcstep(1, 10, 2))
print('1~100 =', calcstep(1, 100))
print('1 =', calcstep(1))
