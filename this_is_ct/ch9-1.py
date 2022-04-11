# 다익스트라 알고리즘
# 음의 간선이 없을 때 정상적으로 동작
# 그리디 알고리즘: 가장 비용이 적은 노드를 매번 선택하기

import sys
INF = sys.maxsize
input = sys.stdin.readline

# number of nodes and edges
n, m = map(int, input().split())
# starting node number
start = int(input())
# node info
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

# edges
for _ in range(m):
    # c is the cost for going from a to b
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# unvisited nearest node
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0  # initialise distance for the starting node
    visited[start] = True  # mark visited
    # update distance for nodes connected to the starting node
    for j in graph[start]:
        distance[j[0]] = j[1]
    # for all nodes but starting node
    for i in range(n - 1):
        # get the nearest node from now
        now = get_smallest_node()
        visited[now] = True
        # check other nodes connected with current node
        for j in graph[now]:
            cost = distance[now] + j[1]  # update cost
            # if distance is shorter when passing by current node, update cost
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)
for i in range(1, n + 1):
    # unreachable, print INF
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
