# {
# 키1:값1
# 키2:값2
# }

dic = {
    'boy': '소년',
    'school': '학교',
    'book': '책'
}
print(dic)  # {'boy': '소년', 'school': '학교', 'book': '책'}


print(dic['boy'])
print(dic['book'])
# print(dic['girl']) 없는값 검색하면 오류발생 프로그램 종료됨

# 있으면 리턴해주고 없으면 특정메세지를 리턴해주는 방법

print(dic.get('boy'))
print(dic.get('girl'))
print(dic.get('girl', '사전에 없는 단어입니다.'))

for i in dic:
    print(i)  # 사전에 있는 키값을 출력한다!!!
