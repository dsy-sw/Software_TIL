dic = {'boy': '소년', 'school': '학교', 'book': '책'}
print(dic.keys())
print(dic.values())
print(dic.items())
# dict_keys(['boy', 'school', 'book'])
# dict_values(['소년', '학교', '책'])
# dict_items([('boy', '소년'), ('school', '학교'), ('book', '책')])

keylist = dic.keys()
for key in dic:
    print(key, dic[key])

    # boy 소년
    # school 학교
    # book 책

for t in dic.items():
    print(t[0], t[1])

    # boy 소년
    # school 학교
    # book 책

for key, value in dic.items():
    print(key, value)

    # boy 소년
    # school 학교
    # book 책

# 세개다 결과는 같다. 밑에 있는 거는 튜플의 특성을 이용한것

li = list(dic.keys())
print(li)   # ['boy', 'school', 'book']

# 사전을 리스트화 하면 키값이 리스트로 출력된다.
li = list(dic)
print(li)   # ['boy', 'school', 'book']