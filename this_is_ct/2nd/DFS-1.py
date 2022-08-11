# Ch 5 - 실전 문제 3. 음료수 얼려 먹기

n, m = map(int, input().split())
graph = [[int(x) for x in input()] for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]


def is_ice(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:  # out of rance
        return False
    if graph[x][y] == 1 or visited[x][y]:  # not ice or already visited
        return False
    return True


def dfs(x, y):
    for dx, dy in zip(dxs, dys):  # try all four
        nx, ny = x + dx, y + dy
        if is_ice(nx, ny):  # if can go
            visited[nx][ny] = True  # mark visited
            dfs(nx, ny)  # try dfs again


cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:  # ice, not visited
            visited[i][j] = True  # mark current place visited
            dfs(i, j)  # try dfs
            cnt += 1  # increment count
print(cnt)
