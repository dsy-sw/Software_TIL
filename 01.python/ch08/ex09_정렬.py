# .sort([reverse=True][key=키에 적용할 함수])
# 리스트를 정렬(디폴트는 오름차순)
# reverse=True 오름차순 reverse=False 내림차순 선택

# .reverse()
# 리스트의 순서를 역으로 바꿈

# sorted(시퀸스)
# 지정한 시퀸스를 정렬하여 새로운 리스트로 리턴

score = [88, 95, 70, 100, 99]

score.sort()
print(score)    # [70, 88, 95, 99, 100]

score.reverse()
print(score)    # [100, 99, 95, 88, 70]

sorted_score = sorted(score)

score = [88, 95, 70, 100, 99]

print(score)         # [88, 95, 70, 100, 99]
print(sorted_score)  # [70, 88, 95, 99, 100]

score = [88, 95, 70, 100, 99]

sorted_score2 = sorted(score, reverse=True)

print(score)          # [88, 95, 70, 100, 99]
print(sorted_score2)  # [100, 99, 95, 88, 70]


country = ['Korea', 'japan', 'CHINA', 'america']

country.sort()
print(country)  # ['CHINA', 'Korea', 'america', 'japan']

country.sort(key=str.lower)
print(country)  # ['america', 'CHINA', 'japan', 'Korea']
