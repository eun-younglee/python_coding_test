
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
steps = [[0] * m for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def is_safe(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0 or visited[x][y]:
        return False
    return True


def bfs():
    q = []
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_safe(nx, ny):
                visited[nx][ny] = True
                steps[nx][ny] = steps[x][y] + 1
                q.append((nx, ny))


bfs()