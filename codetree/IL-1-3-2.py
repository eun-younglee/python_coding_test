# 코드트리 - Intermediate Low - Simulation - 격자 안에서 터지고 떨어지는 경우 - 십자 모양 폭발 

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = [[0] * n for _ in range(n)]
r, c = map(int, input().split())
r, c = r - 1, c - 1  # correction


def in_range(x):
    return 0 <= x < n


def explode():
    # exploded areas to zero
    scale = graph[r][c]
    # horizontal
    for i in range(c - scale + 1, c + scale):
        if in_range(i):
            graph[r][i] = 0
    # vertical
    for i in range(r - scale + 1, r + scale):
        if in_range(i):
            graph[i][c] = 0


def remap():
    for i in range(n):
        temp = []  # put column to new list
        for j in range(n):
            if graph[j][i] > 0:
                temp.append(graph[j][i])
        # put to answer
        cnt = 1
        for j in range(len(temp) - 1, -1, -1):
            answer[n - cnt][i] = temp[j]
            cnt += 1


explode()
remap()
for i in range(n):
    for j in range(n):
        print(answer[i][j], end=" ")
    print()