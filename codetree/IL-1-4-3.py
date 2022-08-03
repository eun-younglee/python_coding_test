# 코드트리 - Intermediate Low - Simulation - 격자 안에서 단일 객체를 이동  - 벽 짚고 미로 탈출하기

n = int(input())
x, y = map(int, input().split())
x, y = x - 1, y - 1
graph = [list(input()) for _ in range(n)]
visited = [[[False for _ in range(4)] for _ in range(n)] for _ in range(n)]
time = 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def wall_exist(x, y):
    return in_range(x, y) and graph[x][y] == '#'


def simulate(x, y, curr_dir):
    time = 0
    while True:
        # if the situation is repeated, cannot escape, return -1
        if visited[x][y][curr_dir]:
            return -1

        visited[x][y][curr_dir] = True
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        nx, ny = x + dxs[curr_dir], y + dys[curr_dir]

        # turn if there is a wall on the front
        if wall_exist(nx, ny):
            curr_dir = (curr_dir - 1) % 4

        # out of grid, escape
        elif not in_range(nx, ny):
            x, y = nx, ny
            time += 1
            return time

        # right front is a wall
        else:
            rx = nx + dxs[(curr_dir + 1) % 4]
            ry = ny + dys[(curr_dir + 1) % 4]

            if wall_exist(rx, ry):
                x, y = nx, ny
                time += 1
            # no wall
            else:
                x, y = rx, ry
                curr_dir = (curr_dir + 1) % 4
                time += 2


result = simulate(x, y, 0)
print(result)
