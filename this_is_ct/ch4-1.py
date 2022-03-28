# 상하좌우

n = int(input())
plans = input().split()

matrix = [[0 for _ in range(n)] for _ in range(n)]
x, y = 0, 0

#    L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direction = {
    "L": 0,
    "R": 1,
    "U": 2,
    "D": 3
}


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


for plan in plans:
    nx, ny = x + dx[direction[plan]], y + dy[direction[plan]]  # next coordinates
    if in_range(nx, ny):  # check if next coordinates is in range
        x, y = nx, ny  # change current coordinate

print(x + 1, y + 1)
