list0 = ['a', 'b']
list1 = [list0, 1, 2]
list2 = list1.copy()  # 얕은 복사 
                      # 데이터값이 전부 복사된것이 아니라 
                      # 참조도 있어서 나중에도 영향을 받는다.

list2[0][1] = 'c'
print(list1)  # [['a', 'c'], 1, 2]
print(list2)  # [['a', 'c'], 1, 2]
print(list0)  # ['a', 'c']