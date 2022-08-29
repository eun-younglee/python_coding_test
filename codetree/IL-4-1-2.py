# 코드트리 - Intermediate Low - BFS - BFS 탐색 - 갈 수 있는 곳들

from collections import deque
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

q = deque()
for _ in range(k):
    x, y = list(map(int, input().split()))
    x, y = x - 1, y - 1
    q.append([x, y])
    visited[x][y] = True


def can_go(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if visited[x][y] or graph[x][y] == 1:
        return False
    return True


def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                q.append([nx, ny])
                visited[nx][ny] = True


bfs()
cnt = sum([1 for i in range(n) for j in range(n) if visited[i][j]])
print(cnt)
