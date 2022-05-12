# 회전판에 있는 음식을 1번부터 차례대로 1초에 하나씩 먹은 다음 다음 음식을 먹는다
# 먹방을 시작한 지 K초 후에 방송이 잠시 중단되었고,
# 방송을 재개할 때 몇 번 음식부터 다시 먹으면 되는지를 출력

import heapq


def solution(food_times, k):
    if sum(food_times) <= k:  # time is larger than all the food, return -1
        return -1

    q = []
    for i in range(len(food_times)):
        # push into queue, (time, number)
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0  # time used to eat
    previous = 0  # previously completed food time
    length = len(food_times)

    # while sum_value + (current food time - previous food time) * current food number < = k
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]  # get food with the smallest time
        sum_value += (now - previous) * length  # add (current food time - previous food time) * current food number
        length -= 1  # one food all eaten
        previous = now  # current food becomes previous

    result = sorted(q, key=lambda x: x[1])  # order according to food number
    return result[(k - sum_value) % length][1]  # find number among leftover food


food_times = list(map(int, input().split()))
k = int(input())
a = solution(food_times, k)
print(a)
