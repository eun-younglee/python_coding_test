# Ch 13 - 기출문제 17. 경쟁적 전염

# n * n 사이즈의 시험관에서 바이러스가 증식
# 번호가 낮은 종류의 바이러스부터 먼저 증식
# S 초 이후에 (x, y)에 존재하는 바이러스의 종류를 출력
# (1, 1) 부터 시작하고 바이러스 존재하지 않으면 0 출력

from collections import deque
n, k = map(int, input().split())
graph, virus = [], []
visited = [[False] * n for _ in range(n)]
steps = [[0] * n for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(n):
        if line[j] > 0:
            virus.append([i, j, line[j]])  # virus location and virus number
            visited[i][j] = True  # visited
s, x, y = map(int, input().split())
x, y = x - 1, y - 1  # adjust


def can_go(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:  # out of range
        return False
    if visited[x][y]:  # visited
        return False
    return True


def bfs():
    q = deque(virus)
    dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
    while q:
        x, y, num = q.popleft()
        if steps[x][y] == s:
            break
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                graph[nx][ny] = num  # contaminate
                visited[nx][ny] = True  # mark visited
                q.append([nx, ny, num])  # put to deque
                steps[nx][ny] = steps[x][y] + 1  # one more step


bfs()
print(graph[x][y])

