s = '0123456789'
print(s[2:5])  # 234
print(s[3:])   # 3456789
print(s[:4])   # 0123
print(s[::2])  # 02468


file = '20200101-104830.jpg'
print('촬영 날짜'+file[4:6]+'월'+file[6:8]+'일')
print('촬영 날짜'+file[9:11]+'월'+file[11:13]+'일')
print('확장자'+file[-3:])


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
