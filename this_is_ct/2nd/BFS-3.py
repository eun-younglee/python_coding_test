# Ch 13 - 기출문제 15. 특정 거리의 도시 찾기

# 연구소는 n * m 직사각형
# 벽을 3개 세울 수 있을 때 안전 영역의 최대 크기
# 0은 빈칸, 1은 벽, 2는 바이러스

from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
virus, empty = [], []
graph = []
visited = [[False] * m for _ in range(n)]
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(m):
        if line[j] == 2:
            virus.append([i, j])
        if line[j] == 0:
            empty.append([i, j])


def can_go(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:  # out of range
        return False
    if visited[x][y] or copy_graph[x][y] == 1 or copy_graph[x][y] == 2:  # visited or wall or already virus
        return False
    return True


def virus_infection():
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):  # infect
                copy_graph[nx][ny] = 2
                visited[nx][ny] = True
                q.append([nx, ny])


def count():  # count all the 0
    cnt = 0
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 0:
                cnt += 1
    return cnt


walls = list(combinations(empty, 3))
copy_graph = copy.deepcopy(graph)
max_safe = 0
for wall in walls:
    for x, y in wall:  # install wall
        copy_graph[x][y] = 1
    virus_infection()  # virus infection
    max_safe = max(max_safe, count())  # count max safe zone
    copy_graph = copy.deepcopy(graph)  # reset copy_graph
    visited = [[False] * m for _ in range(n)]  # reset visited

print(max_safe)
