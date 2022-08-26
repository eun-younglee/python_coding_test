# Ch 13 - 기출문제 20. 감시 피하기
#
# n * n 크기의 복도
# 선생님이 상하좌우 방향으로 감시하며 장애물이 있으면 뒤에 있는 학생은 볼 수 없음
# 선생님은 t, 학생은 s, 장애물은 o
# 장애물을 3개 설치하여 모든 학생이 선생님의 감시를 피할 수 있는지 출력 - YES / NO

from itertools import combinations
from collections import deque
import copy

n = int(input())
graph = []
teachers, empty = [], []
for i in range(n):
    line = list(input().split())
    graph.append(line)
    for j in range(n):
        if line[j] == 'X':  # empty locations
            empty.append([i, j])
        if line[j] == 'T':  # teacher locations
            teachers.append([i, j])


def can_go(x, y, visited):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if visited[x][y]:
        return False
    return True


def check_teachers(teachers):
    visited = [[False] * n for _ in range(n)]
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    q = deque(teachers)
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, visited):
                if graph_new[nx][ny] == 'S':  # found student
                    return False
                if graph_new[nx][ny] == 'O':  # obstacle found, stop
                    break
                if graph_new[nx][ny] == 'X':  # empty, keep searching
                    q.append([nx, ny])
                    visited[nx][ny] = True
    return True


can_escape = False
obstacles = list(combinations(empty, 3))  # get three obstacles

graph_new = copy.deepcopy(graph)
for obstacle in obstacles:
    for ox, oy in obstacle:  # install obstacles
        graph_new[ox][oy] = 'O'
    if check_teachers(teachers):  # check if everyone escapes surveillance
        can_escape = True
        break
    graph_new = copy.deepcopy(graph)  # reset graph

if can_escape:
    print("YES")
else:
    print("NO")
