# is 연산자
# 두 변수가 같은 참조를 가지고 있는지 조사

list1 = ['a', 'b']
list2 = list1
list3 = list1.copy() # 얕은 복사

print("list1 == list2", list1 is list2)
print("list1 == list3", list1 is list3)
print("list2 == list3", list2 is list3)