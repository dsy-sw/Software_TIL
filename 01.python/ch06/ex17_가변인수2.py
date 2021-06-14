# 가중치를 전달해서, 가중치의 곱의 합을 리턴하세요.

def intsum(weight, *ints):  # 가변인수를 뒤로 중요하다~~~!!!!!!
    total = 0
    for num in ints:
        if num < 0:
            return  # return None과 동일
        total += num*weight
    return total


values = range(1, 1000)
print(intsum(0.9, *values))  # intsum(0.9,values)이렇게 돌리면 망함

values = range(1, 5)
print(values)
print(*values)

# 가변인수에 컬렉션을 전달할때는 *을 이용해서 펼쳐서 전달한다.