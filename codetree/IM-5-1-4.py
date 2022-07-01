import sys
import heapq

INF = sys.maxsize
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
route = [0] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # both ways
    graph[a].append((b, c))
    graph[b].append((a, c))

start, end = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        curr_dist, curr_index = heapq.heappop(q)
        if curr_dist != distance[curr_index]:
            continue  # skip duplicates
        for target_index, target_cost in graph[curr_index]:
            cost = curr_dist + target_cost
            if cost < distance[target_index]:
                distance[target_index] = cost
                heapq.heappush(q, (cost, target_index))
                # get previous index
                route[target_index] = curr_index


dijkstra(start)
print(distance[end])

# finding route
endpoint = end
vertices = []
vertices.append(endpoint)

while endpoint != start:  # trace to the start
    endpoint = route[endpoint]
    vertices.append(endpoint)

for num in vertices[::-1]:  # print backwards
    print(num, end=" ")