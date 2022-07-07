# 코드트리 - IntermediateMid - Shortest Path - Dijkstra - 최단거리 3

# 코드트리 - IntermediateMid - Shortest Path - Dijkstra - 최단거리 3

import heapq
import sys

INF = sys.maxsize
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # bidirectional
    graph[b].append((a, c))
start, end = map(int, input().split())


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        curr_cost, curr_index = heapq.heappop(q)
        if curr_cost != distance[curr_index]:
            continue  # duplicates
        for target_index, target_cost in graph[curr_index]: # connected to current node
            cost = curr_cost + target_cost
            if cost < distance[target_index]:
                distance[target_index] = cost
                heapq.heappush(q, (cost, target_index))


dijkstra(start)
print(distance[end])