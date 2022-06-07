# a ~ n까지 도시와 m개의 단방향 도로가 존재
# 특정한 도시 x로부터 출발하여 도달할 수 있는 모든 도시 중
# 최단 거리가 정확히 k인 모든 도시의 번호 출력

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
step = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        now = queue.popleft()
        for next_node in graph[now]:  # check nodes connected to current node
            if not visited[next_node]:  # if next node is not visited
                queue.append(next_node)  # visit next node
                visited[next_node] = True  # mark visited
                step[next_node] = step[now] + 1  # augment one step


bfs(graph, x, visited)
check = False
for i in range(1, m + 1):  # check for k distance from the start
    if step[i] == k:
        print(i)
        check = True
if not check:  # none exists
    print(-1)
