# 퀵 정렬
# 가장 많이 사용됨
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸기
# divide & conquer 알고리즘
# 데이터가 무작위적일 때 더 잘 동작한다

nums = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(nums, start, end):
    if start >= end:  # if there is only one element, end the sorting
        return
    pivot = start  # pivot is the first element
    left = start + 1
    right = end
    while left <= right:  # until left is smaller than the right
        while left <= end and nums[left] <= nums[pivot]:  # until finding bigger number than pivot
            left += 1
        while right > start and nums[right] >= nums[pivot]:  # until finding smaller number than pivot
            right -= 1
        if left > right:  # if left and right is crossed
            # switch because there are smaller elements than pivot
            nums[right], nums[pivot] = nums[pivot], nums[right]
        else:  # not crossed
            # pivot is the smallest number
            nums[left], nums[right] = nums[right], nums[left]
    quick_sort(nums, start, right - 1)  # quick sort fore elements
    quick_sort(nums, right + 1, end)  # quick sort rear elements


quick_sort(nums, 0, len(nums) - 1)
print(nums)
