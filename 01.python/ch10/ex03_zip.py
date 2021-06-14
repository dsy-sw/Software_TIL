info = """ 고길동 홍길동 둘리 도우너
30 40 50 60
70 90 60 56 78
80 100 20 90 100
30 40 50 60"""

info_lines = info.splitlines()
students = info_lines[0].split()      # key파트
scores = info_lines[1:]
print(scores)
# scores = [line.split() for line in scores]  # value파트
# print(scores)
# result = dict(zip(students, scores))
# print(result)

# {'고길동': ['30', '40', '50', '60'],
# '홍길동': ['70', '90', '60', '56', '78'],
# '둘리': ['80', '100', '20', '90', '100'],
# '도우너': ['30', '40', '50', '60']}

# 아직 점수가 문자열이다 숫자로 바까야해 더배워서

# append로도 가능 빈 dic에다가 append와
# for문을이용해서 집어넣는 과정 루프가 많아진다.

scores = [list(map(int, line.split())) for line in scores]
print(scores)
result = dict(zip(students, scores))
print(result)
