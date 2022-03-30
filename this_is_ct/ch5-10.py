# 음료수 얼려 먹기

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def can_go(x, y):
    if not in_range(x, y):
        return False
    if graph[x][y] == 1 or visited[x][y]:
        return False
    return True


def dfs(x, y):
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            visited[nx][ny] = True  # visited
            dfs(nx, ny)


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            dfs(i, j)
            cnt += 1

print(cnt)

