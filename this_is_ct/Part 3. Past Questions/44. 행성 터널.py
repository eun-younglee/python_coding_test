# n개의 행성으로 이루어져 있는 왕국을 지배하기 위해 행성을 연결하는 터널을 만드려 한다
# 행성은 3차원 좌표 위에 있으며, 두 행성을 연결하는 데 드는 비용은
# min(|xa - xb|, |ya - yb|, |za - zb|)
# 터널을 총 n - 1개 걸설해 모든 행성이 연결되게 하려 할 때 필요한 최소 비용

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x


n = int(input())
x, y, z = [], [], []
parent = [0] * (n + 1)
edges = []
result = 0

for i in range(n + 1):
    parent[i] = i

for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

for i in range(n - 1):
    edges.append((abs(x[i + 1][0] - x[i][0]), x[i][1], x[i + 1][1]))
    edges.append((abs(y[i + 1][0] - y[i][0]), y[i][1], y[i + 1][1]))
    edges.append((abs(z[i + 1][0] - z[i][0]), z[i][1], z[i + 1][1]))

edges.sort()
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
