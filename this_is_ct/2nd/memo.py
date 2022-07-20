# Ch 11 - 기출문제 5. 볼링공 고르기
# 회전판에 있는 음식을 1번부터 차례대로 1초에 하나씩 먹은 다음 다음 음식을 먹는다
# 먹방을 시작한 지 K초 후에 방송이 잠시 중단되었고, 방송을 재개할 때 몇 번 음식부터 다시 먹으면 되는지를 출력

import heapq


def solution(food_times, k):
    if sum(food_times) < k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))  # (food left, order)
    total, previous = 0, 0
    length = len(q)
    while total + (q[0][0] - previous) * length <= k:
        food_left, order = heapq.heappop(q)
        total += (food_left - previous) * length
        length -= 1
        previous = food_left
    result = sorted(q, key=lambda x: x[1])  # order by original order
    return result[(k - total) % length][1]


food_times = list(map(int, input().split()))
k = int(input())
answer = solution(food_times, k)
print(answer)
