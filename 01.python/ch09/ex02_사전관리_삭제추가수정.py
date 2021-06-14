dic = {
    'boy': '소년',
    'school': '학교',
    'book': '책'
}
dic['boy'] = '남자아이' # 기존값 수정
dic['girl'] = '소녀'    # 새로운 엔트리 추가
del dic['book']         # 기존 엔트리 삭제
print(dic) 
# {'boy': '남자아이', 'school': '학교', 'girl': '소녀'}
