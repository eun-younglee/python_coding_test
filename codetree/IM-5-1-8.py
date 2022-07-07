# 코드트리 - IntermediateMid - Shortest Path - Dijkstra - 가장 가까운 거리의 최댓값

import heapq
import sys

INF = sys.maxsize
n, m = map(int, input().split())
a, b, c = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
dist_a, dist_b, dist_c = [INF] * (n + 1), [INF] * (n + 1), [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))


def dijkstra(start, distance):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        curr_cost, curr_index = heapq.heappop(q)
        if distance[curr_index] != curr_cost:
            continue
        for target_index, target_cost in graph[curr_index]:
            cost = curr_cost + target_cost
            if cost < distance[target_index]:
                distance[target_index] = cost
                heapq.heappush(q, (cost, target_index))


dijkstra(a, dist_a)
dijkstra(b, dist_b)
dijkstra(c, dist_c)

result = [0]
for i in range(1, n + 1):
    result.append(min(dist_a[i], dist_b[i], dist_c[i]))  # find minimum among three
print(max(result))
