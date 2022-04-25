# DFS

def dfs(v):
    print(v, end = " ")
    for curr_v in graph[v]:  # check all the vertexes connected to the current
        if not visited[curr_v]:
            visited[curr_v] = True  # mark visited
            dfs(curr_v)  # search from there


graph = [
    [], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4],
    [7], [2, 6, 8], [1, 7]
]
visited = [False] * 9

root = 1
visited[root] = True
dfs(root)
