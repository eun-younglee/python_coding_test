# 미로 탈출
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
step = [[0 for _ in range(m)] for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def push(x, y, s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x, y))


def can_go(x, y):
    if not in_range(x, y):
        return False
    if graph[x][y] == 0 or visited[x][y]:
        return False
    return True


def bfs(x, y):
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]
    while q:  # until queue is empty
        x, y = q.popleft()  # get the first input
        for dx, dy in zip(dxs, dys):  # check all four directions
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)  # push into queue, one more step than before


q = deque()
push(0, 0, 1)
bfs(0, 0)
print(step[n - 1][m - 1])  # get the exit's step 
