# 코드트리 - IntermediateMid - Shortest Path - Dijkstra - 천 개의 정거장
# 우선순위 큐로 풀기
# 인접행렬로 나타내야 메모리 초과가 나지 않는다

import sys
import heapq

INF = sys.maxsize
m = 1000  # number of nodes
start, end, n = map(int, input().split())
graph = [[(INF, 0)] * (m + 1) for _ in range(m + 1)]  # (y, cost, time)
distance = [(INF, 0)] * (m + 1)  # (cost, time)

for _ in range(n):
    cost, station_no = map(int, input().split())
    stations = list(map(int, input().split()))
    for i in range(station_no):
        for j in range(i + 1, station_no):
            if graph[stations[i]][stations[j]] > (cost, j - i):
                graph[stations[i]][stations[j]] = (cost, j - i)


def dijkstra(start):
    q = []
    distance[start] = (0, 0)
    heapq.heappush(q, (0, start, 0))  # (cost, y, time)
    while q:
        curr_cost, curr_index, curr_time = heapq.heappop(q)
        if curr_cost != distance[curr_index][0]:
            continue
        for i in range(1, m + 1):
            if graph[curr_index][i] == (INF, 0):
                continue 
            target_cost, target_time = graph[curr_index][i]
            cost = curr_cost + target_cost
            time = curr_time + target_time
            if cost < distance[i][0]:
                distance[i] = (cost, time)
                heapq.heappush(q, (cost, i, time))
            elif cost == distance[i][0]:
                if time < distance[i][1]:
                    distance[i] = (cost, time)
                    heapq.heappush(q, (cost, i, time))


dijkstra(start)
if distance[end] == (INF, 0):
    print(-1, -1)
else:
    print(distance[end][0], distance[end][1])



