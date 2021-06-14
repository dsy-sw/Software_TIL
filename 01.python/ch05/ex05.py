# 다중 if문

age = 23
if age < 19:
    print('애들은 가라')
elif age < 25:
    print('대학생입니다')
else:    # 생략 가능 함
    print('들어오세요')


# 중첩 if문

if age < 19:
    print('애들은 가라')
else:
    if age < 25:
        print('대학생입니다')
    else:    # 생략 가능 함
        print('들어오세요')
