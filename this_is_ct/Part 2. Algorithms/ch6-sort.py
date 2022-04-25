# 파이썬 정렬 라이브러리

nums = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# sorted() returns sorted array
result = sorted(nums)
print(result)

# sort() sorts original array
nums.sort()
print(nums)

# sorting with key parameter
array = [('banana', 2), ('apple', 5), ('orange', 3)]


def setting(data):
    return data[1]


result = sorted(array, key=setting)
print(result)