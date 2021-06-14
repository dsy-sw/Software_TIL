# 람다함수
# 한 줄로 정의되는 함수의 축약표현
# 함수의 이름이 없다.
# 변수에 직접 대입하여 사용.
# 구조 lambda 인수:식

score = [45, 89, 72, 53, 94]
for s in map(lambda x: x/2, score):
    print(s, end=', ')  # 22.5, 44.5, 36.0, 26.5, 47.0,


# 60점 이하인 성적이 포함되어있는지 판단하세요.
# 과락 여부 판단
score = [70, 90, 62, 56, 78]

result = list(map(lambda x: x < 60, score))

print(any(result))

# 모든과목이 통과했냐?
score = [70, 90, 62, 56, 78]

result = list(map(lambda x: x >= 60, score))

print(all(result))
