stack = []

# 스택으로 데이터를 저장해야 됩니다.
stack.append(10)  # 10
stack.append(20)  # 10 20
stack.append(30)  # 10 20 30

# 데이터를 스택에서 꺼내는 것.
v1 = stack.pop()  # 30  /  10 20
v2 = stack.pop()  # 20  /  10

stack.append(40)  # 10 40

# 큐방식 관리(통신에 만이 쓰임 buffer 뒤에 넣고 맨앞에서 빼고)
score = [88, 95, 70, 100, 99]
score.append(50)
print('큐', score)         # 큐 [88, 95, 70, 100, 99, 50]
print('큐', score.pop(0))  # 큐 88
print('큐', score)         # 큐 [95, 70, 100, 99, 50]


# 스택방식 관리 (뒤에 넣고 뒤에서 빼고)
score = [88, 95, 70, 100, 99]
score.append(50)
print('스택', score)        # 스택 [88, 95, 70, 100, 99, 50]
print('스택', score.pop())  # 스택 50
print('스택', score)        # 스택 [88, 95, 70, 100, 99]
