def test1(a):
    a = 20


# 밑의 a와 위의 a는 다르다.
a = 10
test1(a)  # call by value
print(a)  # 10 -> 함수를 호출하고 계산값만 출력하고 사라지기때문에


def test2(l):
    l[0] = 20


l = [1, 2, 3]
test2(l)   # call by ref 참조를 불러서 요소를 바꿔서 원본이 바꼈다.
print(l)   # [20, 2, 3]

# 요소하나를 바꾸면 바뀌고 함수를 만들어서 데이터 전체를 바꾸면 안바뀐다.
