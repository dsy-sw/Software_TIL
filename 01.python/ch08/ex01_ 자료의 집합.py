score = [88, 95, 70, 100, 99]
total = 0

for s in score:
    total += s

print('총점: ', total)               # 총점:  452
print('평균: ', total/len(score))    # 평균:  90.4

print(list('Korea'))                 # ['K', 'o', 'r', 'e', 'a']

# 변수명이랑 함수명이랑 같으면 안된다. 오류는 아니지만
# 함수를 사용하지 못하게 되기때문에~~