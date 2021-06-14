try:
    with open('live.txt', 'rt', encoding='utf-8') as f:
        rows = f.readlines()
        for ix, row in enumerate(rows, 1):
            print(f'{ix}: {row}', end='')

except Exception as e:
    print('예외발생', e)


f = open('live.txt', 'rt',encoding='utf-8')

for line in f:
    print(line, end='')
f.close()
