# 연구소는 n * m 직사각형
# 벽을 3개 세울 수 있을 때 안전 영역의 최대 크기
# 0은 빈칸, 1은 벽, 2는 바이러스
# collection 써서 푸는 방법 찾기
# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
graph = []
virus, empty = [], []
result = 0
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# graph
for i in range(n):
    l = list(map(int, input().split()))
    graph.append(l)
    for j in range(m):
        if l[j] == 0:  # empty locations
            empty.append((i, j))
        if l[j] == 2:  # virus locations
            virus.append((i, j))
graph_wall = copy.deepcopy(graph)


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs():
    q = deque(virus)  # add virus location to queue
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny):  # virus can go
                if graph_wall[nx][ny] == 0:  # empty space
                    graph_wall[nx][ny] = 2  # contaminate
                    q.append((nx, ny))


def calculate_safe():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph_wall[i][j] == 0:
                cnt += 1
    return cnt


def selection():  # select wall locations
    global graph_wall
    safe_zone = 0
    walls = list(combinations(empty, 3))  # choose three locations for wall
    for wall in walls:  # check all possible wall locations
        # install wall - copy wall location
        for w in wall:
            x, y = w
            graph_wall[x][y] = 1
        bfs()
        safe_zone = max(safe_zone, calculate_safe())
        # uninstall wall
        graph_wall = copy.deepcopy(graph)
    return safe_zone


print(selection())
