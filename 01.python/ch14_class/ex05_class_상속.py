class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(str(self.age)+'살'+self.name+'입니다.')


class Player:
    def __init__(self, gender):
        self.gender = gender


class Student(Human, Player):  # 다중상속
    def __init__(self, name, age, gender, stunum):
        # super().__init__(name, age)  # Human.__init__(name,age) 이렇게하면 에러난다.
        Human.__init__(self,name,age)  # 이렇게하면 된다. 다중상속일때 쓴다.
        Player.__init__(self,gender)

        self.stunum = stunum

    def intro(self):
        super().intro()
        print('학번: '+str(self.stunum))

    def study(self):
        print('하늘천 따지 검을 현 누를 황')


kim = Human('김상형', 29)
kim.intro()

lee = Student('이승우', 45, 117149)
lee.intro()
lee.study()
