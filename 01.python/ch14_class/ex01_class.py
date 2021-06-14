# 누구의 계좌인지
# 출금(withdraw)

# 클래스 설계능력이 중요!!

class Human:
    def __init__(self, name, age):       # <--쓸변수는 다넣어준다. 나중에 정의해줄 변수도
        self.name = name                 # 나중에 정의할 변수에는 None을 넣는다
        self.age = age
        self.gender = None

    def intro(self):
        print(f'{self.age}살 {self.name}({self.gender})입니다.')

    def change(self, gender):  # <--class 인자 추가가능 하지만 비권장이다.
        self.gender = gender

    def __str__(self):  # <-----특수 메소드
        return f'<Human {self.age},{self.name},{self.gender}>'

    def __repr__(self):
        return f'<Human {self.name}>'


class Account:
    def __init__(self, owner, balance):  # 생성자 함수
        self.owner = owner  # self.owner.name, self.owner.age, self.owner.gender
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def inquire(self):
        print('잔액은 %d원 입니다.' % self.balance)

    def withdraw(self, money):
        if self.balance < money:
            raise Exception('잔액부족')

        self.balance -= money
        return money


hong = Human('홍길동', 29)
account = Account(hong, 8000)   # Account의 인스턴스 생성
account.deposit(1000)  # <--- ctrl + 클릭시 해당 메소드로 이동 된다.
account.inquire()
try:
    account.withdraw(3000)
    account.inquire()
    account.withdraw(10000)
    account.inquire()
except Exception as e:
    print('예외', e)

# print(account)
