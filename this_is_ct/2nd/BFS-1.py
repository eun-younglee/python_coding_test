# Ch 5 - 실전 문제 4. 미로 탈출

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
steps = [[0] * m for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def is_safe(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if visited[x][y] or graph[x][y] == 0:
        return False
    return True


def push(x, y, step):
    visited[x][y] = True
    steps[x][y] = step + 1
    q.append((x, y))


def bfs(x, y):
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if is_safe(nx, ny):
                push(nx, ny, steps[x][y])


q = deque()
push(0, 0, 0)
bfs(0, 0)
print(steps[n - 1][m - 1])
