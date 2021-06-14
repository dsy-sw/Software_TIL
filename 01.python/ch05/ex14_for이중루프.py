for dan in range(2, 10):
    print(dan, '단')
    for hang in range(2, 10):
        print(dan, '*', hang, '=', dan*hang)
    print()


for y in range(1, 10):
    for x in range(y):
        print('*', end='')
    print()
