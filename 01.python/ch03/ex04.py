print(ord('a'))
print(chr(98))
print(ord('z'))

# print('ABCDEF...Z')
for i in range(1, 10):
    print(i)

# A....Z
for c in range(ord('A'), ord('Z')+1):
    print(chr(c), end='')  # 비어있는 문자열 ''
