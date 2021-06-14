# filter(판정함수, 시퀸스) -> 시퀸스
# ---시퀸스의 각 요소를 판정함수에 전달하여 True를
# ---리턴하는 요소로만 구성된 새로운 시퀸스 리턴


def flunk(s):
    return s < 60


score = [45, 89, 72, 53, 94]
for s in filter(flunk, score):
    print(s)

# 45
# 53
