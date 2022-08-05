# 코드트리 - Intermediate Low - Simulation - 격자 안에서 단일 객체를 이동 - 주사위 던지기

n, m, r, c = map(int, input().split())
x, y = r - 1, c - 1  # rearrange
graph = [[0] * n for _ in range(n)]
maps = input().split()

up, front, right = 1, 2, 3
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]  # U, R, D, L
graph[x][y] = 7 - up  # starting place


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def change(m):
    global up, right, front
    if m == 0:
        up, front = front, 7 - up
    if m == 1:
        right, up = up, 7 - right
    if m == 2:
        front, up = up, 7 - front
    if m == 3:
        right, up = 7 - up, right


def move(direc):
    global x, y
    nx, ny = x + dxs[direc], y + dys[direc]  # see next place
    if in_range(nx, ny):  # if in range
        change(direc)  # roll the dice
        x, y = nx, ny  # update
        graph[x][y] = 7 - up  # write number to new place


direction = {"U": 0, "R": 1, "D": 2, "L": 3}
for m in maps:
    move(direction[m])  # move according to direction


result = list(map(sum, graph))  # sum of each row
print(sum(result))

