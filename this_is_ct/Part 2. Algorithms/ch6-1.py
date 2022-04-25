# 선택 정렬
# 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸기

nums = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# my solution
for i in range(len(nums)):
    minimum = 10
    for j in range(i, len(nums)):
        minimum = min(minimum, nums[j])  # select smallest number after current
    min_index = nums.index(minimum)  # find smallest number's index
    nums[min_index] = nums[i]  # swap
    nums[i] = minimum
print(nums)


# book's solution
for i in range(len(nums)):
    min_index = i  # current index as minimum index
    for j in range(i + 1, len(nums)):
        if nums[min_index] > nums[j]:  # find the smallest number after current
            min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]  # swap
print(nums)
