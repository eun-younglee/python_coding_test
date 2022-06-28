# 성적을 비교한 결과의 일부만을 갖고 있을 때
# 성적 순위를 정확히 알 수 있는 학생이 몇 명인지 계산하기

INF = 1e9
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# initialise oneself route
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# get input
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1  # all cost 1

# calculate
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:  # if reachable
            cnt += 1
    if cnt == n:  # all six nodes reachable
        result += 1
print(result)
