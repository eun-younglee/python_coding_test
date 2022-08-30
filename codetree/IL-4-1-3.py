# 코드트리 - Intermediate Low - BFS - BFS 탐색 - K 번 최댓값으로 이동하기


from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r - 1, c - 1  # adjust locations
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs(r, c):
    visited = [[False] * n for _ in range(n)]
    q = deque([[r, c]])
    value = graph[r][c]
    can_go = []

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and graph[nx][ny] < value:  # meet conditions
                # collect possible positions
                can_go.append([graph[nx][ny], nx, ny])
                q.append([nx, ny])
                visited[nx][ny] = True

    max_value, min_row, min_col = 0, 101, 101
    if len(can_go) == 0:  # no smaller number
        return r, c
    else:  # find location to go
        while can_go:  # check all possible positions
            value, row, col = can_go.pop()
            if value > max_value:
                max_value, min_row, min_col = value, row, col
            if value == max_value:
                if row < min_row:
                    max_value, min_row, min_col = value, row, col
                if row == min_row:
                    if col < min_col:
                        max_value, min_row, min_col = value, row, col
    return min_row, min_col


for i in range(k):
    r, c = bfs(r, c)
print(r + 1, c + 1)