# 코드트리 - Intermediate Mid - Greedy - Greedy - 자연수 M/2개의 쌍

n = int(input())  # m개의 자연수 중 서로 다른 값의 개수
m = 0
numbers = []
for _ in range(n):
    x, y = map(int, input().split())
    numbers.append([x, y])
    m += x

numbers.sort(key=lambda x: x[1])
c = 0
i, j = 0, n - 1
while i <= j:
    x = min(numbers[i][0], numbers[j][0])  # find smaller
    if i == j:
        x = x // 2
    c = max(c, numbers[i][1] + numbers[j][1])  # find maximum sum
    numbers[i][0] -= x
    numbers[j][0] -= x
    if numbers[i][0] == 0:  # all used
        i += 1
    if numbers[j][0] == 0:  # all used
        j -= 1

print(c)
