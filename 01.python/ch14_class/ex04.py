class Human:
    def __init__(self):
        self.name = '홍길동'

    def info(self):
        print(self.name)


def test3(func):
    func()


hong = Human()
test3(hong.info)

hong = Human
# hong.info # <--- 위에 괄호 없어서 self가 없다는 에러 나온다.

h1 = hong()
h1.info()
