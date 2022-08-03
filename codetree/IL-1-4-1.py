# 코드트리 - Intermediate Low - Simulation - 격자 안에서 단일 객체를 이동 - 숫자가 더 큰 인접한 곳으로 이동

n, r, c = map(int, input().split())
x, y = r - 1, c - 1  # rearrange according to list order
graph = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]  # u d l r
answer = [graph[x][y]]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


while True:
    all_four_fail = True
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and graph[nx][ny] > graph[x][y]:  # condition met
            x, y = nx, ny  # update
            answer.append(graph[x][y])
            all_four_fail = False
    if all_four_fail is True:  # all four ways failed
        break

[print(a, end=" ") for a in answer]
