score = [92, 86, 68, 120, 56]
for s in score:
    if (s < 0) or (s > 100):
        break
    print(s)
print('성적 처리 끝')


score = [92, 86, 68, -1, 56]
for s in score:
    if s == -1:
        continue
    print(s)
print('성적 처리 끝')


score = [92, 86, 68, 120, -20, 40, 68, -1, 56]
num = 0
for s in score:
    if (s < 0) or (s > 100):
        num += 1
        continue
    print(s)
print('성적 처리 끝')
print('오류데이터는', num, '개 입니다.')

# 들여쓰기 레벨 한번에 바꾸는 법 블럭잡고 탭 누르기 또는 쉬프트 탭