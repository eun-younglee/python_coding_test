# 연구소는 n * m 직사각형
# 벽을 3개 세울 수 있을 때 안전 영역의 최대 크기
# 0은 빈칸, 1은 벽, 2는 바이러스
#
# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
graph_wall = [[0] * m for _ in range(n)]  # after wall install
result = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def virus(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny):
            if graph_wall[nx][ny] == 0:  # if vacant
                graph_wall[nx][ny] = 2  # contaminate
                virus(nx, ny)


def safe_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if graph_wall[i][j] == 0:
                score += 1
    return score


def dfs(count):
    global result
    # three walls installed
    if count == 3:
        for i in range(n):  # copy graph to test virus
            for j in range(m):
                graph_wall[i][j] = graph[i][j]
        for i in range(n):  # virus simulation from each virus location
            for j in range(m):
                if graph_wall[i][j] == 2:
                    virus(i, j)
        result = max(result, safe_score())
        return
    # wall install
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:  # empty space
                graph[i][j] = 1  # install wall
                count += 1
                dfs(count)  # try dfs
                graph[i][j] = 0   # remove wall
                count -= 1


dfs(0)
print(result)
