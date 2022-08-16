# Ch 13 - 기출문제 15. 특정 거리의 도시 찾기
#
# a ~ n까지 도시와 m개의 단방향 도로가 존재
# 특정한 도시 x로부터 출발하여 도달할 수 있는 모든 도시 중
# 최단 거리가 정확히 k인 모든 도시의 번호 출력

from collections import deque
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [-1] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # go from a to b


distance[x] = 0
q = deque([x])
while q:
    now_city = q.popleft()
    for next_city in graph[now_city]:
        if distance[next_city] == -1:  # not visited
            distance[next_city] = distance[now_city] + 1  # one more
            q.append(next_city)


printed = False
for i in range(1, n + 1):
    if distance[i] == k:
        printed = True
        print(i)
if not printed:
    print(-1)
