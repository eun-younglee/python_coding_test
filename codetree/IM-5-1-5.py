# 코드트리 - IntermediateMid - Shortest Path - Dijkstra - 최단거리 11

import sys

INF = sys.maxsize
n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
distance = [INF] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x][y] = z
    graph[y][x] = z
start, end = map(int, input().split())

distance[end] = 0  # start from the end location
for i in range(n + 1):
    min_index = -1
    for j in range(n + 1):
        if visited[j]:
            continue
        if min_index == -1 or distance[min_index] > distance[j]:
            min_index = j
    visited[min_index] = True

    for j in range(n + 1):
        if graph[min_index][j] == 0:
            continue
        if distance[j] > distance[min_index] + graph[min_index][j]:
            distance[j] = distance[min_index] + graph[min_index][j]

print(distance[start])

x = start
print(x, end=" ")
while x != end:
    for i in range(1, n + 1):
        if graph[i][x] == 0:  # edge doesn't exist
            continue
        if distance[i] + graph[i][x] == distance[x]:
            x = i
            break
    print(x, end=" ")