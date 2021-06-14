price = 500
print('궁금하면 '+str(price)+'원!')


# python 2 기법이다!!!

mont = 8
day = 15
anni = '광복절'
print('%d월 %d일은 %s이다.' % (mont, day, anni))

# python 3는 이렇게 한다.

name = '한결'
age = 16
height = 162.5
print('이름:{}, 나이: {}, 키: {}'.format(name, age, height))
print('이름:{:s}, 나이: {:d}, 키: {:f}'.format(name, age, height))
print('이름:{:4s}, 나이: {:3d}, 키: {:.2f}'.format(name, age, height))
print('이름:{0}, 나이: {1}, 키: {2}'.format(name, age, height))

# python 3.7부터 지원하는 새로운 방법(f-string)
print(f'이름:{name}, 나이: {age}, 키: {height}')
print(f'이름:{name:4s}, 나이: {age:3d}, 키: {height:.2f}')

user1 = f'이름:{name}, 나이: {age}, 키: {height}'
print(user1)


# f-string 예제

socialnum = '001212-3451231'

# '생년-월-일' 로 포맷팅 해서 출력
# 출신 지역 코드 출력

year = socialnum[:2]
month = socialnum[2:4]
date = socialnum[4:6]
region = socialnum[8:10]
gubun = socialnum[7]

if gubun == '1' or gubun == '2':
    year = '19'+year
else:
    year = '20'+year

print('생일:', year+'-'+month+'-'+date)
print('지역코드:', region)

print(f'생일: {year}-{month}-{date}, age: {age}')
print(f'지역코드: {region}')
