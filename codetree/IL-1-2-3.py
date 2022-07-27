# 코드트리 - Intermediate Low - Simulation - 격자 안에서 밀고 당기기 - 1차원 바람

n, m, q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
wind = [tuple(input().split()) for _ in range(q)]  # (row, dir)


def blow_left(row):
    temp = graph[row][m - 1]
    for i in range(m - 1, 0, -1):
        graph[row][i] = graph[row][i - 1]
    graph[row][0] = temp


def blow_right(row):
    temp = graph[row][0]
    for i in range(1, m):
        graph[row][i - 1] = graph[row][i]
    graph[row][m - 1] = temp


def check_duplicates(row):
    # compare between previous
    for i in range(m):
        if graph[row][i] == graph[row + 1][i]:
            return True
    return False


for i in range(q):
    row, direction = int(wind[i][0]) - 1, wind[i][1]
    # input row
    if direction == "R":
        blow_right(row)
    if direction == "L":
        blow_left(row)

    # go up
    prev = direction  # previous dir initialise
    for j in range(row - 1, -1, -1):
        if check_duplicates(j):  # have duplicates
            if prev == "R":
                blow_left(j)
                prev = "L"  # update prev
            else:
                blow_right(j)
                prev = "R"
        else:  # no more duplicate
            break  # no more ripple

    # go down
    prev = direction  # initialise
    for j in range(row, n - 1):
        if check_duplicates(j):  # have duplicates
            if prev == "R":
                blow_left(j + 1)
                prev = "L"  # update prev
            else:
                blow_right(j + 1)
                prev = "R"
        else:  # no duplicate
            break  # no more ripple


for i in range(n):
    for j in range(m):
        print(graph[i][j], end=" ")
    print()
