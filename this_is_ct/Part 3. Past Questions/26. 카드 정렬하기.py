# 카드 묶음을 두 묶음씩 골라 서로 합쳐나갈 때
# 최소한 몇 번의 비교가 필요한지 구하기
import heapq

n = int(input())
card = [10, 20, 40, 50]

# using sort
card.sort()
total = sum(card[:2])
for i in range(1, n - 1):
    add = sum(card[:i + 1])
    total += add + card[i + 1]
print(total)

# using heapq
heap = []
result = 0
for i in range(n):
    heapq.heappush(heap, int(input()))

while len(heap) != 1:
    # two smallest numbers
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    sum_value = first + second
    result += sum_value
    heapq.heappush(heap, sum_value)
print(result)