# .append(값)
# 리스트의 끝에 값을 추가

# .insert(위치, 값)
# 지정한 위치에 값을 삽입

nums = [1, 2, 3, 4]
nums.append(5)
print(nums)  # [1, 2, 3, 4, 5]

nums.insert(2, 99)
print(nums)  # [1, 2, 99, 3, 4, 5]

nums = [1, 2, 3, 4]
nums[2:2] = [90, 91, 92]  # 새로운 값들을 삽입 슬라이싱
print(nums)  # [1, 2, 90, 91, 92, 3, 4]


nums = [1, 2, 3, 4]
nums[2] = [90, 91, 92]  # 지정한 위치의 엘리먼트에 리스트 대체 인덱싱
print(nums)  # [1, 2, [90, 91, 92], 4]


list1 = [1, 2, 3, 4, 5]
list2 = [10, 11]
list3 = list1 + list2  # 새로운 리스트를 리턴
print(list3)   # [1, 2, 3, 4, 5, 10, 11]

list1.extend(list2)  # 기존 리스트를 확장
print(list1)   # [1, 2, 3, 4, 5, 10, 11]
