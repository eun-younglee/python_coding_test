# 위상 정렬(Topology sort)
# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것 ex) 선수과목을 고려한 학습 순서 결정
# 진입차수 - 특정한 노드로 들어오는 간선의 개수

# 위상 정렬 알고리즘
# 진입차수가 0인 노드를 큐에 넣고 큐가 빌 때까지 큐에서 원소를 꺼내
# 해당 노드에서 출발하는 간선을 그래프에서 제거하고 새롭게 진입차수가 0이 된 노드를 큐에 넣는다
# 사이클이 발생하면 원소가 모두 추출되기 전에 큐가 비어버린다

from collections import deque

v, e = map(int, input().split())
# initialise in-degree(진입차수) as 0 for all nodes
in_degree = [0] * (v + 1)
# edge info
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # can move from a to b
    in_degree[b] += 1  # add in degree


def topology_sort():
    result = []  # algorithm result
    q = deque()

    # insert node with 0 in-degree for start
    for i in range(1, v + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:  # until queue is empty
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            in_degree[i] -= 1
            # insert nodes that have 0 in-degree now
            if in_degree[i] == 0:
                q.append(i)

    for i in result:  # print result
        print(i, end=" ")


topology_sort()

