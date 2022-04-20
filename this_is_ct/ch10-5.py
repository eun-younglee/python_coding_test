# 신장 트리(spanning tree)
# 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# 최소 신장 트리 알고리즘 - 신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리 찾기

# 크루스칼 알고리즘
# 그리디 알고리즘, 모든 간선을 정렬하고 가장 거리가 짧은 간선부터 집합에 포함시키기
# 사이클 발생할 간선은 포함시키지 않기

def find_parent(parent, x):
    # if not root node, recursion until finding root node
    if parent[x] != x:  # root node has oneself as parent
        return find_parent(parent, parent[x])
    return parent[x]


# union two sets
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:  # smaller number becomes parent
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)  # initialise parent table

# list for edges and variable for final cost
edges = []
result = 0

# initialise parent as oneself
for i in range(1, v + 1):
    parent[i] = i

# get input
for _ in range(e):
    a, b, cost = map(int, input().split())
    # tuple's first element as cost for ordering by cost
    edges.append((cost, a, b))

# order edges by cost
edges.sort()

for edge in edges:
    cost, a, b = edge
    # include in sets when cycle does not occur
    if find_parent(parent, a) != find_parent(parent, b):  # if parent are not the same
        union_parent(parent, a, b)  # union
        result += cost

print(result)
