# Ch 12 - 기출문제 11. 뱀

# 사과를 먹으면 뱀 길이가 늘어남
# 벽이나 자기 자신의 몸에 부딪히면 게임 오버
# n * n 보드에서 게임이 진행되고, 뱀의 초기 길이는 1이고 맨 위 맨 좌측에 위치
# 뱀은 몸길이를 늘여 머리를 다음 칸에 위치시키고, 사과가 있으면 꼬리 움직이지 않고 없으면 몸길이 줄이기
# 게임이 몇 초에 끝나는지 출력하기

n = int(input())
graph = [[0] * n for _ in range(n)]
# apple
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1  # have apple
# snake
l = int(input())
change = [input().split() for _ in range(l)]  # direction change info, L or D
change_index = 0

snake = []  # snake position
x_head, y_head = 0, 0
headed = 0  # headed right
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]  # E S W N
second = 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


while True:
    # change direction
    if second == int(change[change_index][0]):  # same second
        direction = change[change_index][1]
        if direction == "D":  # turn to the right
            headed = (headed + 1) % 4
        else:  # turn to the left
            headed = (headed - 1) % 4
        if change_index < l - 1:  # update index
            change_index += 1
    temp_x, temp_y = x_head + dxs[headed], y_head + dys[headed]  # head goes to next place
    second += 1  # one second passed
    # bump to a wall or oneself, break
    if not in_range(temp_x, temp_y) or [temp_x, temp_y] in snake:
        break
    if graph[temp_x][temp_y] == 0:  # no apple, remove tail
        if snake:
            snake.pop(0)
    snake.append([x_head, y_head])  # put original head to snake
    x_head, y_head = temp_x, temp_y  # update head

print(second)
