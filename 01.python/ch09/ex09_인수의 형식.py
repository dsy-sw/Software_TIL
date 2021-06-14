# 일반변수, 가변변수,키워드 가변변수 순서로 배치해야한다!!!!
# calcstep('김한슬',99,98,95,89,avg=False)
# calcstep(name, *score,**option)

def calcstep(name, *score, **option):
    print(name)
    total = 0
    for s in score:
        total += s

    print('총점 :', total)
    if(option['avg'] == True):   # 여기서 avg를 꼭 써야 해서 없으면 오류
        print('평균 :', total/len(score))


calcstep('홍길동', 88, 99, 77, avg=True)
calcstep('고길동', 99, 88, 95, 85, avg=False)
# calcstep('둘리', 99, 85, 20, 40, 80) 에러 난다.
