# 식별자(identifier): 변수명, 함수명, 클래스명, 메소드명 등... 주로 개발자가 명명한 이름
# 특정 메모리 위치에 대한 이름
# 참조: 실제 데이터가 있는 위치 정보(메모리 주소)를 값으로 가지는 것
# 파이썬은 상수가 없음.
# -> 모든 식별자는 자신의 값을 변경할 수 있음

def test1():
    print('test1 함수입니다.')


def test2():
    print('test2 함수입니다.')


# func = test1
# func()  # test1()

# func = test2
# func()  # test2()


def test3(func):
    func()


test3(test1)  # test1()
test3(test2)  # test2()
