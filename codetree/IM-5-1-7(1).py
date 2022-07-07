# 코드트리 - IntermediateMid - Shortest Path - Dijkstra - 천 개의 정거장

import sys

INF = sys.maxsize
m = 1000  # number of nodes
start, end, n = map(int, input().split())
graph = [[(INF, 0)] * (m + 1) for _ in range(m + 1)]  # (cost, time)
dist = [(INF, 0)] * (m + 1)  # (cost, time)
visited = [False] * (m + 1)

for i in range(1, m + 1):
    graph[i][i] = (0, 0)  # oneself, no cost

for _ in range(n):
    cost, stop_num = map(int, input().split())
    stops = list(map(int, input().split()))
    for i in range(stop_num):
        for j in range(i + 1, stop_num):  # starting from i + 1 because bus only goes one way
            graph[stops[i]][stops[j]] = min(graph[stops[i]][stops[j]], (cost, j - i))  # (cost, time)

dist[start] = (0, 0)  # starting node, cost and time is 0

for _ in range(m):
    min_index = -1
    for i in range(1, m + 1):
        if visited[i]:  # already visited, pass
            continue
        # find the closest node
        if min_index == -1 or dist[min_index] > dist[i]:
            min_index = i

    visited[min_index] = True
    min_cost, min_time = dist[min_index]

    for i in range(1, m + 1):
        cost, time = graph[min_index][i]
        dist[i] = min(dist[i], (min_cost + cost, min_time + time))

if dist[end] == (INF, 0):
    dist[end] = (-1, -1)

min_cost, min_time = dist[end]
print(min_cost, min_time)
