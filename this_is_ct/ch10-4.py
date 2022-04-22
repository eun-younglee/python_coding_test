# 서로소 집합을 활용한 사이클 판별
# 간선의 개수가 E개일 때 모든 간선을 하나씩 확인하여 매 간선에 대해 union과 find 함수를 호출
# 간선에 방향성이 없는 무방향 그래프에만 적용 가능

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
parent = [0] * (v + 1)  # parent table initialise

# initialise by making themselves a parent
for i in range(1, v + 1):
    parent[i] = i

cycle = False

for i in range(e):  # check each edge
    a, b = map(int, input().split())
    # check if the parent is the same before union
    if find_parent(parent, a) == find_parent(parent, b):  # parent is the same
        cycle = True
        break
    else:
        # union if cycle doesn't occur
        union_parent(parent, a, b)

if cycle:
    print("Cycle occurs")
else:
    print("Cycle does not occur")
