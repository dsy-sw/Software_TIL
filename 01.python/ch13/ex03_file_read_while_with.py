text=""
line=1
try:
    with open('live.txt', 'rt',encoding='utf-8') as f:
        while True:
            row=f.readline()
            if not row: break
            text+=str(line)+" : "+row
            line+=1
except Exception as e:
    print('μμΈλ°μ', e)

print(text)