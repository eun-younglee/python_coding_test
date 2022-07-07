# 코드트리 - IntermediateMid - Shortest Path - Dijkstra - 천 개의 정거장
# 우선순위 큐로 풀기

import sys
import heapq

INF = sys.maxsize
m = 1000  # number of nodes
start, end, n = map(int, input().split())
graph = [[] for _ in range(m + 1)]  # (y, cost, time)
distance = [(INF, 0)] * (m + 1)  # (cost, time)

for _ in range(n):
    cost, station_no = map(int, input().split())
    stations = list(map(int, input().split()))
    for i in range(station_no):
        for j in range(i + 1, station_no):
            graph[stations[i]].append((stations[j], cost, j - i))  # bus only goes one way


def dijkstra(start):
    q = []
    distance[start] = (0, 0)
    heapq.heappush(q, (0, start, 0))  # (cost, y, time)
    while q:
        curr_cost, curr_index, curr_time = heapq.heappop(q)
        if curr_cost != distance[curr_index][0]:
            continue
        for target_index, target_cost, target_time in graph[curr_index]:
            cost = curr_cost + target_cost
            time = curr_time + target_time
            if cost < distance[target_index][0]:
                distance[target_index] = (cost, time)
                heapq.heappush(q, (cost, target_index, time))
            if cost == distance[target_index][0]:
                if time < distance[target_index][1]:
                    distance[target_index] = (cost, time)
                    heapq.heappush(q, (cost, target_index, time))


dijkstra(start)
if distance[end] == (INF, 0):
    print(-1, -1)
else:
    print(distance[end][0], distance[end][1])

