s = 'python programming'

print(len(s))
print(s.find('o'))
print(s.rfind('o'))
print(s.index('r'))
print(s.count('n'))

print('a' in s)
print('z' in s)
print('pro' in s)
print('x'not in s)


name = '홍길동'

if name.startswith('홍'):
    print('홍씨입니다.')

if name.startswith('김'):
    print('김씨입니다.')

file = 'figure.jpg'
if file.endswith('.jpg'):
    print('JPG 그림 파일입니다.')


url = 'https://www.naver.com/blog/travel/seoul.html'

px = url.find(':')
if px != -1:  # px>=0
    protocol = url[:px]
else:
    protocol = '없음'

fx = url.rfind('/')
if fx != -1:
    fname = url[fx+1:]
else:
    fname = '없음'

tx = fname.rfind('.')
if tx != -1:
    ftype = fname[tx+1:]
else:
    ftype = '없음'

print('프로토콜:', protocol)
print('파일명:', fname)
print('파일 종류:', ftype)
