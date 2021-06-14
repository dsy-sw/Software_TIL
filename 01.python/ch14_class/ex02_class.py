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


kim = Human('김상형', 29)
print(kim.name)
kim.name = '홍길동'
print(kim.name)
# kim.gender = '남'
kim.change('남')
kim.intro()

lee = Human('이승우', 45)
lee.change('여')
lee.intro()

# l1 = list((1, 2, 3))  # 변환 함수, list(), int(), dict()...라고 했는데
# print(l1)             # class 배우면 리스트 생성자를 만든거다.
print(kim)            # print(l1)처럼 내부데이터를 보고싶다. 그러면 특수 메소드를 만들어야 한다.
print(lee)

li = [kim, lee]
print(li)
