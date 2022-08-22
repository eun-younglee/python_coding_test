# 코드트리 - Intermediate Low - DFS - DFS 탐색 - 뿌요뿌요

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
explode_cnt = 0


def can_go(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if visited[x][y]:
        return False
    return True


def dfs(x, y):
    global explode_cnt, space_cnt
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny) and graph[x][y] == graph[nx][ny]:
            visited[nx][ny] = True
            space_cnt += 1
            dfs(nx, ny)
    return space_cnt


max_block = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            space_cnt = 1
            visited[i][j] = True
            temp = dfs(i, j)
            if temp >= 4:  # more than 4
                explode_cnt += 1  # explode
            max_block = max(temp, max_block)  # find max block
print(explode_cnt, max_block)
