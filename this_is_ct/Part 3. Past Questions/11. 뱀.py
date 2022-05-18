# 사과를 먹으면 뱀 길이가 늘어남
# 벽이나 자기 자신의 몸에 부딪히면 게임 오버
# n * n 보드에서 게임이 진행되고, 뱀의 초기 길이는 1이고 맨 위 맨 좌측에 위치
# 뱀은 몸길이를 늘여 머리를 다음 칸에 위치시키고, 사과가 있으면 꼬리 움직이지 않고 없으면 몸길이 줄이기
# 게임이 몇 초에 끝나는지 출력하기

# grid information
n = int(input())  # grid width
matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

# apple information
k = int(input())  # number of apples
for _ in range(k):  # apple location marking
    x, y = map(int, input().split())
    matrix[x][y] = 1

# turn information
l = int(input())  # number of turns
# (X, L/D), turn left or right after X seconds from game start
turns = []
for _ in range(l):
    x, c = input().split()
    turns.append((int(x), c))


def change_dir(direction, c):
    if c == "L":  # turn left
        direction = (direction - 1) % 4
    else:  # turn right
        direction = (direction + 1) % 4
    return direction


def is_safe(nx, ny):
    if nx < 1 or nx > n or ny < 1 or ny > n:  # out of grid
        return False
    if matrix[nx][ny] == 2:  # collide to own body
        return False
    return True


def simulate():
    x, y = 1, 1  # starting position
    matrix[x][y] = 2  # snake position on grid
    direction = 0  # heading towards east
    time = 0
    index = 0  # next turn
    snake = [(x, y)]  # tail is first element
    while True:
        # see next coordinates
        nx = x + dx[direction]
        ny = y + dy[direction]
        if is_safe(nx, ny):
            if matrix[nx][ny] == 0:  # no apple
                matrix[nx][ny] = 2  # mark next
                snake.append((nx, ny))
                px, py = snake.pop(0)  # get rid of tail
                matrix[px][py] = 0
            if matrix[nx][ny] == 1:  # yes apple
                matrix[nx][ny] = 2  # mark next
                snake.append((nx, ny))
        else:  # dead
            time += 1
            break
        x, y = nx, ny  # head to next coordinates
        time += 1  # time added
        if index < l and time == turns[index][0]:  # if it's time to turn
            direction = change_dir(direction, turns[index][1])  # change direction
            index += 1
    return time


print(simulate())
