# 화성 탐사 기계가 출발 지점에서 목표 지점까지 이동할 때 항상 최적의 경로를 찾도록
# 각각의 칸을 지나기 위한 비용이 존재
# 왼쪽 맨 위에서 오른쪽 제일 아래까지 가는 최소 비용을 출력하는 프로그램
import heapq

INF = 1e9
t = int(input())  # test cases
for _ in range(t):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]  # starting node cost

    while q:
        dist, x, y = heapq.heappop(q)  # shortest node
        # if already visited node, ignore
        if distance[x][y] < dist:
            continue
        # check connected nodes
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:  # out of range
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:  # if bypassing current node is shorter
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    print(distance[n - 1][n - 1])
