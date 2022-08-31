# 코드트리 - Intermediate Low - BFS - BFS 탐색 - 돌 치우기

from collections import deque
from itertools import combinations
# k: no. of starting points, m: no. of rocks to be cleared
n, k, m = map(int, input().split())
graph, rocks = [], []
for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(n):
        if line[j] == 1:
            rocks.append([i, j])  # rock location
starting = []
for _ in range(k):
    x, y = map(int, input().split())
    starting.append([x - 1, y - 1])
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def can_go(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if visited[x][y] or graph[x][y] == 1:
        return False
    return True


def bfs():
    q = deque(starting)
    for sx, sy in starting:
        visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append([nx, ny])


max_visited = 0
cleared = list(combinations(rocks, m))
for clear in cleared:
    visited = [[False] * n for _ in range(n)]  # reset visited
    for x, y in clear:  # clean rocks
        graph[x][y] = 0
    bfs()
    # count visited
    visit_cnt = sum([1 for i in range(n) for j in range(n) if visited[i][j]])
    max_visited = max(max_visited, visit_cnt)
    for x, y in clear:
        graph[x][y] = 1  # put rocks back
print(max_visited)