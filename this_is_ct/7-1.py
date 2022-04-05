# 순차 탐색 코드

def sequential_search(array, n, target):
    for i in range(n):
        if array[i] == target:
            return i + 1


n = int(input())  # number of inputs
target = input()  # target word
array = list(input().split())  # list of words

print(sequential_search(array, n, target))
