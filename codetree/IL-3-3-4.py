# 코드트리 - Intermediate Low - Simulation - 격자 안에서 터지고 떨어지는 경우 - 2048

graph = [list(map(int, input().split())) for _ in range(4)]
direc = input()


def left():
    # add
    for i in range(4):
        prev, prev_index = graph[i][0], 0
        for j in range(1, 4):
            if graph[i][j] == 0:  # pass if 0
                continue
            if prev == graph[i][j]:  # if same
                graph[i][prev_index] = graph[i][prev_index] * 2  # double the cost
                graph[i][j] = 0  # make it to 0
            prev, prev_index = graph[i][j], j  # update
    # push to the left
    for i in range(4):
        numbers = list(filter(lambda x: x > 0, graph[i]))
        if len(numbers) < 4:
            for _ in range(4 - len(numbers)):
                numbers.append(0)
        answer.append(numbers)


def right():
    # add
    for i in range(4):
        prev, prev_index = graph[i][3], 3
        for j in range(2, -1, -1):
            if graph[i][j] == 0:
                continue
            if prev == graph[i][j]:  # if same
                graph[i][prev_index] = graph[i][prev_index] * 2
                graph[i][j] = 0
            prev, prev_index = graph[i][j], j
    # push to the right
    for i in range(4):
        numbers = list(filter(lambda x: x > 0, graph[i]))
        if len(numbers) < 4:
            for _ in range(4 - len(numbers)):
                numbers.insert(0, 0)
        answer.append(numbers)


def up():
    # add
    for j in range(4):
        prev, prev_index = graph[0][j], 0
        for i in range(1, 4):
            if graph[i][j] == 0:
                continue
            if prev == graph[i][j]:  # if same
                graph[prev_index][j] = graph[prev_index][j] * 2
                graph[i][j] = 0
            prev, prev_index = graph[i][j], i
    # push to up
    for i in range(4):
        numbers = list(filter(lambda x: x > 0, [row[i] for row in graph]))
        if len(numbers) < 4:
            for _ in range(4 - len(numbers)):
                numbers.append(0)
        for j in range(4):
            answer[j][i] = numbers[j]


def down():
    # add
    for j in range(4):
        prev, prev_index = graph[3][j], 3
        for i in range(2, -1, -1):
            if graph[i][j] == 0:
                continue
            if prev == graph[i][j]:  # if same
                graph[prev_index][j] = graph[prev_index][j] * 2
                graph[i][j] = 0
            prev, prev_index = graph[i][j], i

    # push to up
    for i in range(4):
        numbers = list(filter(lambda x: x > 0, [row[i] for row in graph]))
        if len(numbers) < 4:
            for _ in range(4 - len(numbers)):
                numbers.insert(0, 0)
        for j in range(4):
            answer[j][i] = numbers[j]


if direc == 'L':
    answer = []
    left()
if direc == 'R':
    answer = []
    right()
if direc == 'U':
    answer = [[0] * 4 for _ in range(4)]
    up()
if direc == 'D':
    answer = [[0] * 4 for _ in range(4)]
    down()

for i in range(4):
    for j in range(4):
        print(answer[i][j], end=" ")
    print()
