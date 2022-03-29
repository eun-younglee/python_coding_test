#  왕실의 나이트

current = input()
x = int(current[1]) - 1
y = ord(current[0]) - ord('a')  # change to the number
matrix = [[0 for _ in range(8)] for _ in range(8)]
dxs = [-1, 1, 2, 2, 1, -1, -2, -2]
dys = [-2, -2, -1, 1, 2, 2, 1, -1]
cnt = 0


def in_range(x, y):
    return 0 <= x < 8 and 0 <= y < 8


for dx, dy in zip(dxs, dys):
    nx, ny = x + dx, y + dy  # see possible coordinates
    if in_range(nx, ny):  # check if in range
        cnt += 1

print(cnt)
