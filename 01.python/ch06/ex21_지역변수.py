def kim():
    temp = '김과장의 함수'
    print(temp)


temp = 'Hello'
print(temp)   # Hello
kim()         # 김과장의 함수
print(temp)   # Hello

# 지역변수인 temp는 함수를 호출했을때만 
# 전역변수 메모리에 저장되었다가 함수가 끝나면 삭제된다.
