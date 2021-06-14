def calcstep(**args):
    begin = args['begin']   # 사전의 키를 이용해서 불러내는 방법
    end = args['end']
    step = args['step']

    total = 0
    for num in range(begin, end+1, step):
        total += num
    return total


print('3 ~ 5 =', calcstep(begin=3, end=5, step=1))
print('3 ~ 5 =', calcstep(step=1, end=5, begin=3))
