# int : 정수    ->int(12.34) -> 12
# float : 실수  ->
# str : 문자열  ->
a = 1234
print(type(a))
a='string'
print(type(a))

price=input('가격을 입력하세요 : ')
num=input('수량을 입력하세요 : ')
sum=int(price)*int(num)
print('총액은',sum,'원 입니다.')