# 코드트리 - Intermediate Mid - Shortest Path - Dijkstra - 가장 오래 걸리는 학생 2

import heapq
import sys

INF = sys.maxsize
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))  # append in opposite


def dijkstra(destination):
    q = []
    heapq.heappush(q, (0, destination))
    distance[destination] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist != distance[now]:  # already visited
            continue
        for target_index, target_dist in graph[now]:
            cost = dist + target_dist
            if cost < distance[target_index]:
                distance[target_index] = cost
                heapq.heappush(q, (cost, target_index))


dijkstra(n)
print(max(distance[1:]))