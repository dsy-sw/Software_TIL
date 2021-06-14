class Car:

    @staticmethod        # 인스턴스와 무관하게 사용할 수 있다.
    def hello():
        print('오늘도 안전 운행 합시다.')

    count = 0

    def __init__(self, name):
        self.name = name
        Car.count += 1

    @classmethod
    def outcount(cls):
        print(cls.count)


pride = Car('프라이드')
korando = Car('코란도')
Car.outcount()
Car.hello()
