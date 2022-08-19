# 코드트리 - Intermediate Low - DFS - DFS 탐색 - 두 방향 탈출 가능 여부

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
vil_cnt, population = 0, []
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def is_person(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:  # not in range
        return False
    if visited[x][y] or graph[x][y] == 0:  # already visited or wall
        return False
    return True


def dfs(x, y):
    global vil_pop
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if is_person(nx, ny):
            visited[nx][ny] = True
            vil_pop += 1
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        # not visited and not a wall
        if not visited[i][j] and graph[i][j] == 1:
            visited[i][j] = True
            vil_pop = 1  # population
            vil_cnt += 1
            dfs(i, j)
            population.append(vil_pop)


print(vil_cnt)
population = sorted(population)
for p in population:
    print(p)