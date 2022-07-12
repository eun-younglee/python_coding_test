# 코드트리 - IntermediateMid - Greedy - Greedy - 쪼개어 배낭 채우기 구현

n, m = map(int, input().split())
jewerly = []
for _ in range(n):
    w, p = map(int, input().split())
    jewerly.append((p / w, w, p))  # (value, weight, price)

jewerly.sort(reverse=True)  # order by richest value
steal = 0
for v, w, p in jewerly:
    if w <= m:  # weight lighter than the size
        steal += v * w  # value added
        m -= w  # minus weight
    else:  # more weight than the size
        steal += v * m
        break
print("{:.3f}".format(steal))  # up to 3 decimals
