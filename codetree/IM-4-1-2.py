# 코드트리 - IntermediateMid - Greedy - Greedy - 연속 부분 합의 최댓값 구하기 2
import sys

n = int(input())
numbers = list(map(int, input().split()))
max_sum = numbers[0]
answer = -sys.maxsize

for i in range(1, n):
    if max_sum < 0:
        max_sum = numbers[i]  # reset because below zero
    else:
        max_sum += numbers[i]  # add next number
    answer = max(answer, max_sum)  # find maximum
print(answer)
