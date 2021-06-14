# 1~100 번위에서 10개의 랜덤한 숫자로된 리스트를 구성하세요.
import random

# 난수표에서 특정한 난수 조합을 사용한다. 몇번을 돌려도 같은 난수집합으로
# 개발과정중에는 고정하고 개발이 끝나면 지우면 된다.
# random.seed(0)

numbers = [random.randrange(1, 101) for _ in range(10)]
print(numbers)

# 두개의 요소를 서로 바꿔주는 함수

def swap(ix1, ix2):
    temp = numbers[ix1]
    numbers[ix1] = numbers[ix2]
    numbers[ix2] = temp

swap(2, 4)
print(numbers)

# 최대값을 찾아서, 0번과 바꾸세요.

max_value = max(numbers)
max_ix = numbers.index(max_value)

swap(0, max_ix)
print(numbers)

# 정렬하기

# 오름차순
for i in range(0, len(numbers)):
    max_value = max(numbers[i:])
    max_ix = numbers.index(max_value)
    swap(i, max_ix)

print(numbers)

# 내림차순
for i in range(0, len(numbers)):
    min_value = min(numbers[i:])
    min_ix = numbers.index(min_value)
    swap(i, min_ix)

print(numbers)