# 1 ~ n 번까지의 헛간 중에서 하나를 골라 숨을 수 있고
# 술래는 항상 1번 헛간에서 출발
# m개의 양방향 통로가 존재하며 양방향임
# 최단 거리가 가장 먼 헛간이 안전하다고 판단할 때 숨을 헛간의 번호 출력
# 출력:  숨어야 하는 헛간 번호, 그 헛간까지의 거리, 그 헛간과 같은 거리를 갖는 헛간의 개수
# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2

import heapq

INF = 1e9
n, m = map(int, input().split())
distance = [INF] * (n + 1)
graph = [[] for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))  # goes both ways
    graph[b].append((a, 1))  # a to b / b to a is cost 1


def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))  # starting node is 1, distance is 0
    distance[1] = 0  # distance is 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:  # already visited
            continue
        for i in graph[now]:  # check nodes connected to current node
            cost = dist + i[1]
            if cost < distance[i[0]]:  # found shorter distance
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra()
maximum = max(distance[1:])  # choose maximum cost
result = []
for i in range(1, n + 1):
    if distance[i] == maximum:
        result.append(i)
print(min(result), maximum, len(result))
