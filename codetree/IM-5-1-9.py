# 코드트리 - IntermediateMid - Shortest Path - Dijkstra - 다른 괄호로 이동하기

import heapq
import sys

INF = sys.maxsize
n, a, b = map(int, input().split())
graph = [list(map(str, input())) for _ in range(n)]


def dijkstra(start_x, start_y):
    q = []
    distance = [[INF] * n for _ in range(n)]
    distance[start_x][start_y] = 0  # starting node distance is 0
    visited = [[False] * n for _ in range(n)]
    heapq.heappush(q, (0, start_x, start_y))
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    max_cost = 0
    while q:
        curr_cost, curr_x, curr_y = heapq.heappop(q)
        if visited[curr_x][curr_y]:  # pass if visited
            continue
        visited[curr_x][curr_y] = True
        for dx, dy in zip(dxs, dys):  # search all four ways
            nx, ny = curr_x + dx, curr_y + dy
            if 0 <= nx < n and 0 <= ny < n:  # in range
                if graph[nx][ny] == graph[curr_x][curr_y]:  # same bracket
                    cost = distance[curr_x][curr_y] + a
                else:  # different bracket
                    cost = distance[curr_x][curr_y] + b
                if cost < distance[nx][ny]:  # if newly calculated cost is smaller than the original
                    distance[nx][ny] = cost  # update the cost
                    heapq.heappush(q, (cost, nx, ny))  # put to the heapq
    return distance


answer = 0
for i in range(n):
    for j in range(n):
        dist = dijkstra(i, j)
        for d in dist:
            answer = max(answer, max(d))
print(answer)
