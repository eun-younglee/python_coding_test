#  게임 개발
#  바다 1 육지 0

n, m = map(int, input().split())
x, y, face = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
cnt = 1
matrix[x][y] = 2  # mark current visited


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def can_go(x, y):
    if not in_range(x, y):
        return False
    if matrix[x][y] == 1 or matrix[x][y] == 2:  # is sea or already visited
        return False
    else:
        return True


def check_four(x, y):
    all_four = 0
    for dx, dy in zip(dxs, dys):  # check all four directions
        nx, ny = x + dx, y + dy
        if not can_go(nx, ny):
            all_four += 1
    if all_four == 4:  # all four directions are visited/sea
        return True
    else:
        return False


def check_back(x, y):
    face_opposite = (face + 2) % 4  # opposite face
    nx, ny = x + dxs[face_opposite], dys[face_opposite]
    if matrix[nx][ny] == 2:  # can go back
        return True
    else:  # cannot go back
        return False


while True:
    if check_four(x, y):  # check if all four directions are visited/sea
        if check_back(x, y):  # go back
            face_opposite = (face + 2) % 4  # opposite face
            x, y = x + dxs[face_opposite], y + dys[face_opposite]
        else:  # cannot go back, end moving
            break
    face = (face - 1 + 4) % 4  # turn to left
    nx, ny = x + dxs[face], y + dys[face]  # check next coordinates
    if can_go(nx, ny):
        x, y = nx, ny  # change current coordinates
        cnt += 1  # count visited
        matrix[x][y] = 2  # mark visited

print(cnt)
