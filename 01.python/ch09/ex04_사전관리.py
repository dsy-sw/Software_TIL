# 사전은 키값이 중복될수있어서 +연산자 사용 불가
# 그래서 .update 메소드를 사용해서 덮어써서 추가한다.

dic = {'boy': '소년', 'school': '학교', 'book': '책'}
dic2 = {'student': '학생', 'teacher': '선생님', 'book': '서적'}

dic.update(dic2)
print(dic)

# {'boy': '소년',
# 'school': '학교',
# 'book': '서적',
# 'student': '학생',
# 'teacher': '선생님'}