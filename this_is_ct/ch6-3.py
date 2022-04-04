# 삽입 정렬
# 데이터를 하나씩 확인하여 각 데이터를 적절한 위치에 삽입하기
# 필요할 때만 위치를 바꾸기 때문에 데이터가 거의 정렬되어 있을 때 효율적
# 두 번째 데이터부터 시작(첫번째 데이터는 정렬되어 있다고 판단)

nums = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(nums)):
    for j in range(i, 0, -1):  # move to the left
        if nums[j - 1] > nums[j]:  # if current is smaller than previous one
            nums[j], nums[j - 1] = nums[j - 1], nums[j]  # swap
        else:  # stop if you meet smaller data than current
            break
print(nums)