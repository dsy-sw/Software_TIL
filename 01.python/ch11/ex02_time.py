import time

t = time.time()

print(t)
print(time.ctime(t))
print(time.localtime(t))

# 현재시간은 t생략가능
t = time.localtime(t)
print(f'{t.tm_year}-{t.tm_mon}-{t.tm_mday}')
# HH:MM:SS
print(f'{t.tm_hour}:{t.tm_min}:{t.tm_sec}')


from datetime import datetime as dt

now = dt.now()
print(f'{now.year}년 {now.month}월 {now.day}일')
print(f'{now.hour}:{now.minute}:{now.second}')
