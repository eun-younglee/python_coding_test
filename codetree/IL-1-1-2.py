# 코드트리 - Intermediate Low - Simulation - 격자 안에서 완전탐색 - 행복한 수열의 개수

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0
# vertical
for i in range(n):
    cnt, max_cnt = 1, 1
    prev = graph[i][0]  # first number
    for j in range(1, n):
        if prev == graph[i][j]:  # same consecutive number
            cnt += 1
        else:  # not consecutive
            cnt = 1  # reset count
            prev = graph[i][j]  # change number
        max_cnt = max(max_cnt, cnt)  # find maximum count
    if max_cnt >= m:
        answer += 1

# horizontal
for i in range(n):
    cnt, max_cnt = 1, 1
    prev = graph[0][i]  # first number
    for j in range(1, n):
        if prev == graph[j][i]:  # same consecutive number
            cnt += 1
        else:  # not consecutive
            cnt = 1  # reset count
            prev = graph[j][i]  # change number
        max_cnt = max(max_cnt, cnt)
    if max_cnt >= m:
        answer += 1
print(answer)