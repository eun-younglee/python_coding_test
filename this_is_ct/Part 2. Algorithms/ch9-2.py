# 힙을 사용한 더욱 빠른 다익스트라 알고리즘
# 최소 힙 구조를 사용하여 비용이 적은 노드를 우선적으로 방문
# (거리, 노드) 튜플을 우선순위 큐에 넣었다가 빼기
# 거리가 가장 짧은 노드를 우선순위 큐가 알아서 선택해준다

import heapq
import sys

INF = sys.maxsize
n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    q = []
    # initialise
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # until there are no more left
        # get closest distance element
        dist, now = heapq.heappop(q)
        if dist != distance[now]:  # already visited, ignore
            continue
        # check all nodes connected to current node
        for target_index, target_dist in graph[now]:
            cost = dist + target_dist
            # bypassing current node is shorter
            if cost < distance[target_index]:
                distance[target_index] = cost  # update cost
                heapq.heappush(q, (cost, target_index))  # put it in heap


dijkstra(start)
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
