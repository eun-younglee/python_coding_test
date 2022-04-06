# 이진 탐색

def binary_search(array, start, end, target):
    if start > end:  # cannot find the target
        return None
    middle = (start + end) // 2
    if target == array[middle]:
        return middle + 1
    elif target > array[middle]:  # if target is larger than middle value
        return binary_search(array, middle + 1, end, target)  # search rear part
    else:  # if target is smaller than middle value
        return binary_search(array, start, middle - 1, target)  # search fore part


n = int(input())  # number of inputs
target = int(input())  # target number
array = list(map(int, input().split()))  # list of numbers

result = binary_search(array, 0, n - 1, target)
if result is None:
    print("Not in the array")
else:
    print(result)
