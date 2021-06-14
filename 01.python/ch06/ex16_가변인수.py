#


def intsum(weight, *ints): # 가변인수를 뒤로 중요하다~~~!!!!!!
    total = 0
    for num in ints:
        if num < 0:
            return  # return None과 동일
        total += num*weight
    return total


print(intsum(1.1, 1, 2, 3))
print(intsum(1.5, 5, 7, 9, 11, 13))
print(intsum(0.8,8, 9, 6, 2, 9, 7, 5, 8))

total = intsum(8, 9, 6, 2, -9, 7, 5, 8)
if total:
    print('total=', total)
else:
    print('잘못된 데이터를 포함하고 있습니다.')