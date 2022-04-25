# 도시 분할 계획

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


n, m = map(int, input().split())
edges = []
result = 0
parent = [0] * (n + 1)

# initialise parent as oneself
for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    # tuple's first element as cost for ordering by cost
    edges.append((c, a, b))

# order edges by cost
edges.sort()
largest = 0

for edge in edges:
    cost, a, b = edge
    # include in sets when cycle does not occur
    if find_parent(parent, a) != find_parent(parent, b):  # if parent are not the same
        union_parent(parent, a, b)  # union
        result += cost
        largest = cost

print(result - largest)