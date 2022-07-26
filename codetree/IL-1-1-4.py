# 코드트리 - Intermediate Low - Simulation - 격자 안에서 완전탐색 - 금 채굴하기

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


def get_area(k):
    return k * k + (k + 1) * (k + 1)


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def get_gold(x, y, k):
    total = 0
    for i in range(n):
        for j in range(n):
            if abs(x - i) + abs(y - j) <= k:  # within diamond range
                total += graph[i][j]
    return total


max_gold = 0
for x in range(n):
    for y in range(n):
        for k in range(2 * n - 1):
            gold = get_gold(x, y, k)
            if gold * m >= get_area(k):
                max_gold = max(max_gold, gold)
print(max_gold)
