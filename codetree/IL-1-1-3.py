# 코드트리 - Intermediate Low - Simulation - 격자 안에서 완전탐색 - 트로미노 

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dxs_l, dys_l = [1, 1, 1, 0], [-1, 0, 1, 1]
dxs_i, dys_i = [1, 2, 0, 0], [0, 0, 1, 2]
shapes_l = [[0, 1], [2, 3], [1, 2], [1, 3]]
shapes_i = [[0, 1], [2, 3]]


def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False


max_sum = 0
for x in range(n - 1):
    for y in range(m - 1):
        # L shaped block
        for block_1, block_2 in shapes_l:
            block_sum = 0
            nx1, ny1 = x + dxs_l[block_1], y + dys_l[block_1]
            nx2, ny2 = x + dxs_l[block_2], y + dys_l[block_2]
            if in_range(nx1, ny1) and in_range(nx2, ny2):
                block_sum += graph[x][y]
                block_sum += graph[nx1][ny1]
                block_sum += graph[nx2][ny2]
            max_sum = max(block_sum, max_sum)
        # - shaped block
        for block_1, block_2 in shapes_i:
            block_sum = 0
            nx1, ny1 = x + dxs_i[block_1], y + dys_i[block_1]
            nx2, ny2 = x + dxs_i[block_2], y + dys_i[block_2]
            if in_range(nx1, ny1) and in_range(nx2, ny2):
                block_sum += graph[x][y]
                block_sum += graph[nx1][ny1]
                block_sum += graph[nx2][ny2]
            max_sum = max(block_sum, max_sum)

print(max_sum)