# 반복문 이진탐색

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return mid + 1
        elif target > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return None


n, target = map(int, input().split())
array = list(map(int, input().split()))
answer = binary_search(array, target, 0, n - 1)
if answer is None:
    print("{} not found".format(target))
else:
    print("{} found in location {}".format(target, answer))