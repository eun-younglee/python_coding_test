# 코드트리 - Intermediate Mid - Shortest Path - Dijkstra - 각 정점까지의 최단 경로 

import sys

INF = sys.maxsize
n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x][y] = z  # directed graph

distance[1] = 0  # starting node
for i in range(1, n + 1):
    # find the closest node among not visited nodes
    min_index = -1
    for j in range(1, n + 1):
        if visited[j]:  # already visited
            continue
        # find closest node
        if min_index == -1 or distance[min_index] > distance[j]:
            min_index = j
    visited[min_index] = True

    # check connected nodes from current node
    for j in range(1, n + 1):
        if graph[min_index][j] == 0:  # edge doesn't exist, pass
            continue
        # update distance
        distance[j] = min(distance[j], distance[min_index] + graph[min_index][j])

for i in range(2, n + 1):
    if distance[i] == INF:
        print(-1)
    else:
        print(distance[i])
