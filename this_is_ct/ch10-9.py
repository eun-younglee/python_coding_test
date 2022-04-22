# 커리큘럼

import copy
from collections import deque

v = int(input())
# initialise in-degree as 0 for all nodes
in_degree = [0] * (v + 1)
# edge info
graph = [[] for i in range(v + 1)]
time = [0] * (v + 1)

for i in range(1, v + 1):
    subject = list(map(int, input().split()))
    time[i] = subject[0]
    for x in subject[1: -1]:
        graph[x].append(i)
        in_degree[i] += 1


def topology_sort():
    result = copy.deepcopy(time)  # algorithm result
    q = deque()

    # insert node with 0 in-degree for start
    for i in range(1, v + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:  # until queue is empty
        now = q.popleft()
        for i in graph[now]:
            result[i] = result[now] + time[i]
            in_degree[i] -= 1
            # insert nodes that have 0 in-degree now
            if in_degree[i] == 0:
                q.append(i)

    for i in range(1, v + 1):
        print(result[i])


topology_sort()
