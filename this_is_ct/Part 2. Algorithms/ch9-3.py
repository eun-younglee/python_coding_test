# 플로이드 워셜 알고리즘
# 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우
# 해당 노드를 중간에 거쳐 지나가는 모든 경우를 고려
# 시간 복잡도 O(N^3)
import sys

INF = sys.maxsize

n = int(input())  # node no.
m = int(input())  # edge no.
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# initialise distance from oneself
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# initialise with input
for _ in range(m):
    # c is the distance from a to b
    a, b, c = map(int, input().split())
    graph[a][b] = c

# from a to b passing by k
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# print the result
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()