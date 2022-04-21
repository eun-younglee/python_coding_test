# 팀 결성

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
parent = [0] * (n + 1)

# initialise by making themselves a parent
for i in range(1, n + 1):
    parent[i] = i 

for _ in range(m):
    way, a, b = map(int, input().split())
    if way == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("Yes")
        else:
            print("No")

