import copy

list0 = ['a', 'b']
list1 = [list0, 1, 2]
list2 = copy.deepcopy(list1) # 깊은 복사

list2[0][1] = 'c'
print(list1)  # [['a', 'b'], 1, 2]
print(list2)  # [['a', 'c'], 1, 2]


def test(l):
    l=[10,20,30]

l=[1,2,3]
test(l)
print(l)      # [1, 2, 3]
