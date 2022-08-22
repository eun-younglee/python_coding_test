# 코드트리 - Intermediate Low - DFS - DFS 탐색 - 안전지대

import copy, sys
sys.setrecursionlimit(2000)
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
max_height = max([max(line) for line in graph])


def can_go(x, y, height):
    if x < 0 or x >= n or y < 0 or y >= m:  # out of range
        return False
    if visited[x][y] or graph[x][y] <= height:  # visited or submerged
        return False
    return True


def dfs(x, y, height):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, height):
            visited[nx][ny] = True
            dfs(nx, ny, height)


def comfort_zone(height):
    cnt = 0
    for i in range(n):
        for j in range(m):
            # not visited, not submerged
            if can_go(i, j, height):
                visited[i][j] = True
                dfs(i, j, height)
                cnt += 1
    return cnt


max_comfort, max_index = -1, -1
for i in range(1, max_height + 1):
    visited = [[False] * m for _ in range(n)]  # reset visited
    cz = comfort_zone(i)  # find comfort zone numbers
    if cz > max_comfort:  # find maximum comfort zone
        max_comfort = cz
        max_index = i
print(max_index, max_comfort)
