import time

start = time.time()
for a in range(1000):
    print(a)       # I/O 작업 입출력작업은 오래걸림
end = time.time()

print(end-start)

# 계산작업은 엄청빠르다.
total = 0
start = time.time()
# 1000번 루프돌며 계산
for a in range(1000):
    total += a
end = time.time()
print(end-start)

# 입출력을 줄여야 처리속도를 빠르게 할수있다.