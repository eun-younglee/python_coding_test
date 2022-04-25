# 힙을 사용한 더욱 빠른 다익스트라 알고리즘
# 최소 힙 구조를 사용하여 비용이 적은 노드를 우선적으로 방문
# (거리, 노드) 튜플을 우선순위 큐에 넣었다가 빼기
# 거리가 가장 짧은 노드를 우선순위 큐가 알아서 선택해준다

import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())  # node / edge numbers
start = int(input())  # starting node number
graph = [[] for i in range(n + 1)]  # node info
distance = [INF] * (n + 1)  # distance initialise

for _ in range(m):
    a, b, c, = map(int, input().split())
    # c is the cost for going from a to b
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # push starting node
    distance[start] = 0  # distance of the starting node is 0
    while q:  # unless queue is empty
        # shortest node
        dist, now = heapq.heappop(q)
        # ignore if cost in distance is already smaller
        if distance[now] < dist:
            continue
        # check nodes connected with current node
        for i in graph[now]:
            cost = dist + i[1]  # current distance + distance to other node(i[1])
            # if distance is shorter when passing by current node, update cost
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
