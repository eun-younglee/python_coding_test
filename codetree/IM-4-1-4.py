# 코드트리 - IntermediateMid - Greedy - Greedy - 숫자 합치기

import heapq

n = int(input())
numbers = list(map(int, input().split()))
cost = 0
q = []

for number in numbers:
    heapq.heappush(q, number)

while len(q) > 1:
    min_1 = heapq.heappop(q)  # smallest number
    min_2 = heapq.heappop(q)  # second-smallest number
    result = min_1 + min_2
    heapq.heappush(q, result)  # put to added number back to heapq
    cost += result  # sum to the cost
print(cost)
