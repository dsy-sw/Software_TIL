nums = list(range(0, 10))

print(nums[:])            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[2:5])          # [2, 3, 4]
print(nums[:4])           # [0, 1, 2, 3]
print(nums[6:])           # [6, 7, 8, 9]
print(nums[1:7:2])        # [1, 3, 5]


# 리스트 요소 수정

nums[2] = 100
print(nums)

s = 'python'    # 숫자는 가능한데 왜 문자열은 안될까?
# s[2] = 'T'      # 문자열은 불변 객체이기 때문에 안된다!
print(s)        # 읽기만 가능하고 쓰기는 불가능


# 기존값을 삭제하고 , 새로운 값으로 대체 (삽입)

nums = list(range(0, 10))
nums[2:5] = [20, 30, 40]
print(nums)
# [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]

nums[6:8] = [60, 70, 80, 90]
print(nums)
# [0, 1, 20, 30, 40, 5, 60, 70, 80, 90, 8, 9]

# 리스트와 연산자

list1 = [1, 2, 3, 4, 5]
list2 = [10, 11]
print(list1+list2)   # [1, 2, 3, 4, 5, 10, 11]
print(list2*3)       # [10, 11, 10, 11, 10, 11]

# 이중 리스트

#          0        1          2
#       0  1  2    0  1    0  1  2  3
lol = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(lol[0])           # [1, 2, 3]
print(lol[2][1])        # 7  # 리스트안의 리스트의 요소

for sub in lol:
    for item in sub:
        print(item, end=' ')
    print()

# 1 2 3
# 4 5
# 6 7 8 9

# 이중 리스트 예제

score = [
    [88, 76, 92, 98], 
    [65, 70, 58, 82], 
    [82, 80, 78, 88]]

total = 0
totalsub = 0

for student in score:
    subject_total = 0                  # subject_total -> snake 표기법
    for subject in student:            # subjectTotalSum -> CamelCase(낙타 표기법)
        subject_total += subject       # subject-total -> 케밥 표기법(HTML)

    subjects = len(student)
    print(f'총점 {subject_total}, 평균 {subject_total/subjects:.2f}')
    total += subject_total
    totalsub += subjects

# 총점 354, 평균 88.50
# 총점 275, 평균 68.75
# 총점 328, 평균 82.00

print(f'전체평균 {total/totalsub:.2f}')

# 전체평균 79.75
