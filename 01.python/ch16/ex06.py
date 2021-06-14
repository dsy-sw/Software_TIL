def inner():
    print('결과를 출력합니다.')


def outer(func):
    print('-'*20)
    func()
    print('-'*20)


outer(inner)


def hello():
    print('안녕하세요')


outer(hello)
