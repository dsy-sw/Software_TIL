s = '짜장 짬뽕 탕수육'
print(s.split())

s2 = '서울->대전->대구->부산'
cities = s2.split('->')
print(cities)

for city in cities:
    print(city)


url = 'https://www.naver.com/blog/travel/seoul.html'

els = url.split('://')
print(els[0])  # https
print(els[1])  # www.naver.com/blog/travel/seoul.html

path = els[1].split('/')
fname = path[-1]
print(fname)

ftype = fname.split('.')[-1]
print(ftype)


travler = """
강나루 거너서
밀밭 길을

구름에 달 가듯이
가는 나그네
"""

poet = travler.splitlines()
for line in poet:
    print(line)
