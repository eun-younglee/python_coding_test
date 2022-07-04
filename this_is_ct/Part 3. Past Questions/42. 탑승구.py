# G개의 탑승구가 있을 때 P개의 비행기가 차례대로 도착
# 비행기를 최대 몇 대 도킹할 수 있는지 구하기

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


g = int(input())  # gate
p = int(input())  # plane
parent = [0] * (g + 1)

for i in range(g + 1):  # initialise
    parent[i] = i
result = 0
for _ in range(p):
    data = find_parent(parent, int(input()))
    if data == 0:  # if root is 0, cannot dock anymore
        break
    union_parent(parent, data, data - 1)  # union with previous node
    result += 1
print(result)

