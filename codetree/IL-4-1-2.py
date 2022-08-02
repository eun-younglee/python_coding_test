# 코드트리 - Intermediate Low - Simulation - 격자 안에서 단일 객체를 이동 - 떨어지는 1자 블록

n, m, k = map(int, input().split())  # 1 * m dropped from kth to k + mth
k = k - 1  # adjust k
graph = [list(map(int, input().split())) for _ in range(n)]
stop = 0


def put_block(i):
    for j in range(k, k + m):
        graph[i][j] = 1


def find_end():
    for i in range(n - 1):
        # check if the block meets 1
        # if do, stop and break
        for j in range(k, k + m):
            if graph[i + 1][j] == 1:
                stop = i
                return i
    return n - 1


i = find_end()
put_block(i)

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=" ")
    print()
