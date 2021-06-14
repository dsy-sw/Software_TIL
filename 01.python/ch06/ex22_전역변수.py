salerate = 0.9


def kim():
    print('오늘의 할인율:', salerate)


def lee():
    price = 1000
    print('가격 :', price*salerate)


kim()
salerate = 1.1
lee()


price = 1000


def sale():
    price = 500   # 지역변수라서 밑에 출력값이랑 다르다.


sale()
print(price)

price = 1000


def sale():
    global price
    price = 500   # global을 이용해서 전역변수로 사용할수있다.


sale()
print(price)


price = 1000


def sale():
    price = 500
    print('sale', id(price))


sale()
print('global', id(price))