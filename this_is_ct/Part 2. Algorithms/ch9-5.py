# 전보

import heapq
import sys
INF = sys.maxsize

n, m, c = map(int, input().split())  # node no. / edge no. / city c
start = c  # starting city is c
graph = [[] for i in range(n + 1)]  # node info
distance = [INF] * (n + 1)  # distance initialise

for _ in range(m):
    a, b, c, = map(int, input().split())
    # c is the distance for going from a to b
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # push starting node
    distance[start] = 0  # distance of the starting node is 0
    while q:  # unless queue is empty
        # shortest node
        dist, now = heapq.heappop(q)
        # ignore if cost in distance is already smaller
        if distance[now] != dist:
            continue
        # check nodes connected with current node
        for target_index, target_dist in graph[now]:
            cost = dist + target_dist  # current distance + distance to other node(i[1])
            # if distance is shorter when passing by current node, update cost
            if cost < distance[target_index]:
                distance[target_index] = cost
                heapq.heappush(q, (cost, target_index))


dijkstra(start)
cnt, max_time = 0, 0
for i in range(1, n + 1):
    if distance[i] != INF:
        cnt += 1
        max_time = max(max_time, distance[i])

print(cnt - 1, max_time)  # cnt - 1 because minus the starting city

