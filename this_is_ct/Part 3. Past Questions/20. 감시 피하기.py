# n * n 크기의 복도
# 선생님이 상하좌우 방향으로 감시하며 장애물이 있으면 뒤에 있는 학생은 볼 수 없음
# 선생님은 t, 학생은 s, 장애물은 o
# 장애물을 3개 설치하여 모든 학생이 선생님의 감시를 피할 수 있는지 출력 - YES / NO
# 5
# X S X X T
# T X S X X
# X X X X X
# X T X X X
# X X T X X

from itertools import combinations
from collections import deque
import copy

n = int(input())
graph = []
spaces, teachers = [], []
for i in range(n):
    l = list(input().split())
    graph.append(l)
    for j in range(n):
        if l[j] == "X":
            spaces.append((i, j))  # (i, j) is blank space
        if l[j] == "T":
            teachers.append((i, j))  # (i, j) is teacher's location


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs():
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    q = deque(teachers)  # add teacher locations to queue
    graph_obs = copy.deepcopy(graph)  # make new graph for obstacle test
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny):
                if graph_obs[nx][ny] == 'S':  # student found, return False
                    return False
                if graph_obs[nx][ny] == 'O':  # obstacle found, cannot search this direction anymore, break
                    break
                x, y = nx, ny
    return True


# choose three spots for obstacles
obs_comb = list(combinations(spaces, 3))  # choose three spaces for obstacle
check = False
for obs in obs_comb:
    for x, y in obs:
        graph[x][y] = 'O'  # install obstacle
    if bfs():  # search students, if found check True
        check = True
        break
    for x, y in obs:
        graph[x][y] = 'X'  # remove obstacle

if check:
    print("YES")
else:
    print("NO")


