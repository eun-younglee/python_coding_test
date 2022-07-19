# Ch 11 - 기출문제 5. 볼링공 고르기
# 회전판에 있는 음식을 1번부터 차례대로 1초에 하나씩 먹은 다음 다음 음식을 먹는다
# 먹방을 시작한 지 K초 후에 방송이 잠시 중단되었고, 방송을 재개할 때 몇 번 음식부터 다시 먹으면 되는지를 출력
import heapq


def solution(food_times, k):
    if sum(food_times) <= k:  # no more food left to eat
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))  # (left food, order)
    length = len(food_times)
    sum_value = 0  # time used to eat
    previous = 0

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now, order = heapq.heappop(q)
        sum_value += (now - previous) * length  # amount of food eaten until now
        length -= 1
        previous = now  # update
    result = sorted(q, key=lambda x: x[1])  # order by orignal order
    return result[(k - sum_value) % length][1]


food_times = list(map(int, input().split()))
k = int(input())
answer = solution(food_times, k)
print(answer)
