# 코드트리 - Intermediate Low - BFS - BFS 탐색 - 네 방향 탈출 여부 확인하기

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def can_go(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if visited[x][y] or graph[x][y] == 0:
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
            if nx == n - 1 and ny == m - 1:
                return True
    return False


q = deque()
q.append([0, 0])
visited[0][0] = True
answer = bfs()

if answer:
    print(1)
else:
    print(0)