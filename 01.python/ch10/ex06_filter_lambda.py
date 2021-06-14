# 람다함수

score = [45, 89, 72, 53, 94]

for s in filter(lambda s: s < 60, score):
    print(s)


# 문장(statement)
# 표현식(expression) --> 값
score2 = list(filter(lambda a: a < 60, score)) # 람다함수 사용
print(score2)


score2 = [n for n in score if n < 60]          # for-in-if
print(score2)
