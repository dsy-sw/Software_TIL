# list는 참조형이기 때문에 전역저장소에
# list가 저장되고 데이터는 mm에 heap에 저장된다.
# list를 부르면 참조값을 사용하여
# heap에 저장된 데이터를 불러오는 정도이기 때문에 참조형이다.

# 스택에 저장되는 데이터는 한번 저장되면 크기가 지정된다.

list1 = [1, 2, 3]
list2 = list1   # 기존의 list1의 참조값을 list2에 복사한다.
# 데이터를 복사한게 아니라 참조값을 복사한거

print(list1 == list2)  # True

list2[1] = 100    # heap에 있는 데이터를 바꿧다.

# 그러므로 list1의 데이터값이 바꿨기 때문에 밑에와 같은 결과가 나온다
print(list1)           # [1, 100, 3]
print(list2)           # [1, 100, 3]

print(list1 == list2)  # True

# 리스트 사본만들기
# .copy()메소드를 사용하여 만듬

list1 = [1, 2, 3]
list2 = list1.copy()

print(list1 == list2) # True 참조값이 아닌 데이터를 보고 비교한다.

list2[1] = 100
print(list1)  # [1, 2, 3]
print(list2)  # [1, 100, 3]

print(list1 == list2)  # False
