def inner():
    print('결과를 출력합니다.')


def outer(func):
    def wrapper():
        print('-'*20)
        func()
        print('-'*20)
    return wrapper


inner = outer(inner)
inner()
