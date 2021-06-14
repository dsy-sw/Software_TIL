# map은 매개변수로 함수를 넣어 전달하는 기능이 있다.
# functional programming(함수적 프로그래밍): filter, map, sort

def total(s, b):
    return s+b


score = [45, 89, 72, 53, 94]
bonus = [2, 3, 0, 0, 5]
for s in map(total, score, bonus):
    print(s, end=", ")    # 47, 92, 72, 53, 99,


score = ['20', '30', '50', '90']
# score=[20,30,50,90]
# for ix, s in enumerate(score):
#    score[ix] = int(s)

#print(score)    # [20, 30, 50, 90]


score = ['20', '30', '50', '90']
# score=[20,30,50,90]

score = list(map(int, score))
print(score)    # [20, 30, 50, 90]
