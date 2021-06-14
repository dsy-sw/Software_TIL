import time
score = (88, 95, 70, 100, 99)  # score = 88, 95, 70, 100, 99 똑같다 튜플표시 방법
total = 0

for s in score:
    total += s

print('총점 : ', total)              # 총점 :  452
print('평균 : ', total/len(score))   # 평균 :  90.4

# 튜플로 슬라이싱이나 새로운 값을 추가하는 것은 가능하지만
# 원본을 변화하는 것은 불가

tu = 1, 2, 3, 4, 5
print(tu[3])        # 4
print(tu[1:4])      # (2, 3, 4)
print(tu + (6, 7))  # (1, 2, 3, 4, 5, 6, 7)
print(tu * 2)       # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# tu[1] = 100 # 불가능
# del tu[1] # 불가능tu[1] = 100 # 불가능
# del tu[1] # 불가능


# 튜플로 가능한 일

names = "이순신", "김유신", "강감찬"
lee, kim, kang = names  # unpack

print(lee)   # 이순신
print(kim)   # 김유신
print(kang)  # 강감찬


a, b = 12, 34
print(a, b)  # 12 34

a, b = b, a   # swap하는거다 튜플이라서 가능
print(a, b)  # 34 12


def gettime():
    now = time.localtime()
    return now.tm_hour, now.tm_min


result = gettime()
print('지금은 %d시 %d분 입니다.' % (result[0], result[1]))

hour, minute = gettime()
print('지금은 %d시 %d분 입니다.' % (hour, minute))


d, m = divmod(7, 3)
print("몫", d)     # 몫 2
print("나머지", m)  # 나머지 1


score = [88, 95, 70, 100, 99]
tu = tuple(score)
print(tu)     # (88, 95, 70, 100, 99)

li = list(tu)
li[0] = 100
print(li)     # [100, 95, 70, 100, 99]
