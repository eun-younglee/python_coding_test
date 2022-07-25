# 코드트리 - Intermediate Low - Simulation - 격자 안에서 완전탐색 - 최고의 33 위치

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
total = 0

for i in range(n - 2):
    for j in range(n - 2):
        square_sum = 0
        for x in range(3):  # seek 3 from now
            for y in range(3):  # seek 3 from now
                square_sum += graph[i + x][j + y]
        total = max(total, square_sum)  # find maximum
print(total)
