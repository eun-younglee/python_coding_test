# 고정점: 수열의 원소 중에서 그 값이 인덱스와 동일한 원소
# 모든 원소가 오름차순으로 정렬되어 있을 때 고정점이 있다면 고정점을 출력
# 없으면 -1 출력, 시간복잡도 O(logN)

n = int(input())
array = list(map(int, input().split()))


def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == mid:  # if index is same as the number
        return mid
    elif array[mid] > mid:  # x smaller than mid, search left
        return binary_search(array, start, mid - 1)
    else:  # x larger than mid, search right
        return binary_search(array, mid + 1, end)


answer = binary_search(array, 0, n - 1)
if answer:
    print(answer)
else:
    print(-1)
