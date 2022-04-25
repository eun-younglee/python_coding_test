# 서로소 집합
# union-find 자료구조라고도 불림
# 각 집합은 노드로, union 관계는 엣지로 나타냄
# 번호가 작은 노드가 부모, 번호가 큰 노드가 자식

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

# union
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# print root set each set belongs to
print("root set:", end=" ")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")
print()

# parent table
print("parent table:", end=" ")
for i in range(1, v + 1):
    print(parent[i], end=" ")