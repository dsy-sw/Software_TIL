# zip 두개의 다른 튜플을 서로 대응하는
# 위치의 요소끼리 묵어서 튜플로 출력하는 함수
# zip은 루프한번만 돌수있다. 계속 쓸려면 list로 묶어서 사용.(중요)

dates = ['월', '화', '수', '목', '금', '토', '일']
food = ['갈비탕', '순대국', '칼국수', '삼겹살']

menu = list(zip(dates, food))    # zip를 list화 시킨거
for d, f in menu:
    print("%s요일 메뉴: %s" % (d, f))


# zip을 dict화 시키는거

menu_dic = dict(zip(dates, food))
print(menu_dic)
# {'월': '갈비탕', '화': '순대국', '수': '칼국수', '목': '삼겹살'}