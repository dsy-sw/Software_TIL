# 다른 파일에 정의된 변수,함수,객체 등을 사용하기 전에 이를 알리는 것
# 표준모듈=파이썬에서 제공하는 모듈

# 구조
# import 모듈 [as alias]  [as alias]는 너무 긴 모듈이름을 짧게 부르겠다.
# from 모듈 import 함수명  모듈에서 필요한 함수만 불러오겠다.

# math모듈 전부에서 불러올때
# import math
# print(math.sqrt(2))

# math모듈에서 특정함수만 불러올때
# from math import sqrt, sin, cos
# print(sqrt(2))

# 서로다른 모듈에 같은이름의 함수를 두개다 쓰고 싶을때
# import A
# import B
# A.sum()
# B.sum()

# 이렇게 많이씀
# imprt random as r
# r.random()

import statistics as st

score = [30, 40, 50, 60, 70, 80, 90]
print(st.mean(score))
print(st.harmonic_mean(score))
print(st.median(score))
print(st.median_low(score))
print(st.median_high(score))
