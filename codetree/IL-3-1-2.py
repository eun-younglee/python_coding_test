# 코드트리 - Intermediate Low - DFS - DFS 탐색 - 두 방향 탈출 가능 여부

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dxs, dys = [1, 0], [0, 1]


def can_go(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:  # not in range
        return False
    if graph[x][y] == 0 or visited[x][y]:  # snake, already visited
        return False
    return True


def dfs(x, y):
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy  # try new location
        if can_go(nx, ny):  # can to
            visited[nx][ny] = True
            dfs(nx, ny)  # dfs from there


visited[0][0] = True
dfs(0, 0)
if visited[n - 1][m - 1]:
    print(1)
else:
    print(0)