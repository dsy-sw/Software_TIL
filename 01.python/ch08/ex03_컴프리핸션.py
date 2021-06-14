# [수식 for 변수 in 리스트 if 조건]

print([n for n in range(1, 11)])
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nums = [n*2 for n in range(1, 11)]
for i in nums:
    print(i, end=', ')
    # 2, 4, 6, 8, 10, 12, 14, 16, 18, 20,

nums = [n*2 for n in range(1, 11) if n % 2 == 0]
for i in nums:
    print(i, end=', ')
    # 4, 8, 12, 16, 20,

nums = []
for n in range(1, 11):
    nums.append(n*2)

print(nums)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print([n for n in range(1, 11) if n % 3 == 0])
# [3, 6, 9]


# 랜덤 정수 100개를 리스트에 담아라. 머지이게

import random            # random.randrange(1,101)

random_numbers = [random.randrange(1, 101) for _ in range(50)] # for n in 인데 n을 안 쓸 경우 _로 대체

print(random_numbers)

random_numbers=[]
for _ in range(50):
    random_numbers.append(random.randrange(1,101))

print(random_numbers)
