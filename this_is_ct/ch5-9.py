# BFS
from collections import deque


def push(i):
    visited[i] = True  # mark visited
    q.append(i)  # append to the queue


def bfs():
    while q:  # while queue is not empty
        v = q.popleft()  # get first input
        print(v, end=" ")
        for i in graph[v]:  # search vertexes connected to current
            if not visited[i]:
                push(i)


graph = [
    [], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4],
    [7], [2, 6, 8], [1, 7]
]
visited = [False] * 9
q = deque()
push(1)
bfs()
