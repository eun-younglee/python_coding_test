# n * n 크기의 땅이 있을 때 각 땅에는 나라가 하나씩 존재하며
# r행 c열에 있는 나라에는 A[r][c] 명이 살고 있다
# 국경선을 공유하는 두 나라의 인구 차이가 l명 이상, r명 이하면 국경선을 하루 동안 연다
# 이동 가능한 나라끼리는 연합 구성
# 인구 이동이 더 이상 발생하지 않을 때까지 지속
# 각 나라의 인구수가 주어졌을 때, 인구 이동이 몇 번 발생하는지 구하기

from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]


def bfs(x, y):
    # countries connected to (x, y) country
    q = deque()
    q.append((x, y))
    united = [(x, y)]
    visited[x][y] = True
    total = graph[x][y]  # total graph of current union
    cnt = 1  # no. of countries of current union
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:  # can go
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # add to the union
                    visited[nx][ny] = True  # mark visited
                    total += graph[nx][ny]  # add population
                    united.append((nx, ny))  # add to union
                    cnt += 1  # one more country added
    # average population for union
    for i, j in united:
        graph[i][j] = total // cnt
    return cnt  # check population migration


move_cnt = 0
while True:
    visited = [[False] * n for _ in range(n)]
    check = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:  # not visited
                if bfs(i, j) > 1:  # check nearby countries
                    check = True
    if not check:  # no more migrations
        break
    move_cnt += 1
print(move_cnt)
