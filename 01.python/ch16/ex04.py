def calcsum(n):
    def add(a, b):   # 함수안에 함수 함수밖에서는 호출불가능!!!!
        return a+b

    total = 0
    for i in range(n+1):
        total = add(total, i)

    return total


print('~ 10 = ', calcsum(10))

# print(add(9, 10)) # not defind
