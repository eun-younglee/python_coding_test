# 코드트리 - Intermediate Low - DFS - DFS 탐색 - 그래프 탐색

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1  # bidirectional
    graph[y][x] = 1


def dfs(node):
    global cnt
    for curr_node in range(1, n + 1):
        # check connected and not visited
        if graph[node][curr_node] and not visited[curr_node]:
            visited[curr_node] = True   # visit
            cnt += 1
            dfs(curr_node)  # dfs from there


visited[1] = True
dfs(1)
print(cnt)
