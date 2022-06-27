# n개의 도시가 있고, 한 도시에서 출발하여 다른 도시에 도착하는 m개의 버스가 있을 때
# 모든 도시의 쌍 (A, B)에 대하여 A에서 B로 가는 데 필요한 비용의 최솟값 구하기
# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4

n = int(input())
m = int(input())
bus = [[100001] * (n + 1) for _ in range(n + 1)]

# initialise oneself route
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            bus[a][b] = 0

# get input
for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a][b] = min(bus[a][b], c)

# calculate
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            bus[a][b] = min(bus[a][b], bus[a][k] + bus[k][b])

# print results
for a in range(1, n + 1):
    for b in range(1, n + 1):
        print(bus[a][b], end=" ")
    print()
