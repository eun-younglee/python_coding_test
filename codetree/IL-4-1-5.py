

from collections import deque
n, m = map(int, input().split())
graph, waters, glaciers = [], [], []
for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(m):
        if line[j] == 0:  # is water
            waters.append([i, j])
        if line[j] == 1:  # is glacier
            glaciers.append([i, j])
second, melt = 0, 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def check_water(wx, wy):
    visited = [[False] * m for _ in range(n)]
    visited[wx][wy] = True
    all_four = 0
    # all four ways meet 1, return True
    for i in range(4):
        q = deque([[wx, wy]])
        while q:
            x, y = q.popleft()
            nx, ny = x + dxs[i], y + dys[i]
            if in_range(nx, ny) and not visited[nx][ny]:
                if graph[nx][ny] == 0:  # is water
                    q.append([nx, ny])
                    visited[nx][ny] = True
                if graph[nx][ny] == 1:  # is glacier, count glacier
                    all_four += 1
                    break
    if all_four == 4:
        return True
    else:
        return False


def melt_ice():
    melt = []
    for gx, gy in glaciers:
        for i in range(4):  # check all four ways
            nx, ny = gx + dxs[i], gy + dys[i]
            if in_range(nx, ny) and graph[nx][ny] == 0:
                melt.append([gx, gy])
                break
    return melt


def all_melt():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:  # glacier left, return False
                return False
    return True


intact_waters = waters
while not all_melt():
    # check all the waters, if surrounded by ice, put 2
    no_melt = []
    for wx, wy in intact_waters:  # check all the waters
        if check_water(wx, wy):  # surrounded by ice
            graph[wx][wy] = 2  # change to 2
            no_melt.append([wx, wy])
    melted = melt_ice()  # list of glaciers that will be melted
    for mx, my in melted:  # melt glaciers
        graph[mx][my] = 0
        glaciers.remove([mx, my])
    # get waters back to 0
    for nmx, nmy in no_melt:
        graph[nmx][nmy] = 0
    second += 1  # one second passed
    intact_waters = no_melt

print(second, len(melted))
