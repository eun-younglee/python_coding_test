# n * n 사이즈의 시험관에서 바이러스가 증식
# 번호가 낮은 종류의 바이러스부터 먼저 증식
# S 초 이후에 (x, y)에 존재하는 바이러스의 종류를 출력
# (1, 1) 부터 시작하고 바이러스 존재하지 않으면 0 출력

from collections import deque

n, k = map(int, input().split())
graph, data = [], []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            # (virus type, time, x, y)
            data.append((graph[i][j], 0, i, j))
sec, x, y = map(int, input().split())

data.sort()  # low number virus spreads first
q = deque(data)


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs():
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]
    while q:
        virus, s, x, y = q.popleft()
        if s == sec:  # exact seconds passed
            break
        for dx, dy in zip(dxs, dys):  # check all four directions
            nx, ny = x + dx, y + dy
            if in_range(nx, ny):
                graph[nx][ny] = virus  # contaminate
                q.append((virus, s + 1, nx, ny))  # add to the queue


bfs()
print(graph[x - 1][y - 1])
