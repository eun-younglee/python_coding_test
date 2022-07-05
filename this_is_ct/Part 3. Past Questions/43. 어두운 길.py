# n개의 집, m개의 도로
# 특정 도로의 가로등을 하루 동안 켜기 위한 비용은 해당 도로의 길이와 동일
# 두 집이 가로등 켜진 도로만으로도 오갈 수 있도록 만들고
# 일부 가로등 비활성화하여 최대한 많은 금액 절약하고자할 때 절약할 수 있는 최대 금액

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * n
edges = []
result = 0

for i in range(n):  # parent table initialise
    parent[i] = i

for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))  # cost comes first for sorting

edges.sort()
total = 0

for edge in edges:
    cost, a, b = edge
    total += cost
    if find_parent(parent, a) != find_parent(parent, b):  # no cycle, don't delete
        union_parent(parent, a, b)  # union
        result += cost

print(total - result)
