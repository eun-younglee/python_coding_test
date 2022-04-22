from collections import deque
import copy

v = int(input())  # no. of vertex
in_degree = [0] * (v + 1)
time = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for i in range(1, v + 1):
    lect = list(map(int, input().split()))
    time[i] = lect[0]   # lecture time
    for t in lect[1:-1]:  # pre required lectures
        graph[t].append(i)
        in_degree[t] += 1


def topology_sort():
    q = deque()
    result = copy.deepcopy(time)

    # starting vertex
    for i in range(1, v + 1):
        if in_degree[i] == 0:
            q.append(i)

    # check edges starting from current vertex
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)

    for i in range(1, v + 1):
        print(result[i])


topology_sort()