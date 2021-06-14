score = [88, 95, 70, 100, 99, 88, 78, 50]
score.remove(100)
print(score)   # [88, 95, 70, 99, 88, 78, 50]

del(score[2])
print(score)   # [88, 95, 99, 88, 78, 50]

score[1:4] = []
print(score)   # [88, 78, 50]

# 삭제를 하는데 그 값이 뭔지 궁금할때

# .pop()
# 인덱스가 없으면 리스트의 끝 요소를 삭제하고 삭제한 요소를 리턴

score = [88, 95, 70, 100, 99]
print(score.pop())     # 99
print(score.pop())     # 100
print(score.pop(1))    # 95
print(score)           # [88, 70]
