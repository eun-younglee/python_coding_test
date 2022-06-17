# n개의 원소를 포함하고 있는 수열이 오름차순으로 정렬
# x가 등장하는 회수를 계산
# 시간 복잡도 O(logN)으로 계산하기

n, x = map(int, input().split())
numbers = list(map(int, input().split()))


def count(numbers, x, n):
    f = first(numbers, x, 0, n - 1)
    if f == 0:  # x doesn't exist
        return 0
    l = last(numbers, x, 0, n - 1)
    return l - f + 1


def first(numbers, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if mid == 0 or numbers[mid - 1] < target == numbers[mid]:  # x exists on the left
        return mid
    elif numbers[mid] >= target:  # x smaller than mid, search left
        return first(numbers, target, start, mid - 1)
    else:  # x larger than mid, search right
        return first(numbers, target, mid + 1, end)


def last(numbers, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if mid == n - 1 or numbers[mid + 1] > target == numbers[mid]:  # x exists on the last element
        return mid
    elif numbers[mid] > target:  # x smaller than mid, search left
        return last(numbers, target, start, mid - 1)
    else:  # x larger than mid, search right
        return last(numbers, target, mid + 1, end)


answer = count(numbers, x, n)
if answer == 0:  # x doesn't exist
    print(-1)
else:
    print(answer)