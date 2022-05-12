n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()
count = [0] * (m + 1)
total = 0

for w in weight:
    count[w] += 1

for i in range(1, m + 1):
    first = count[i]
    for j in range(i + 1, m + 1):
        second = count[j]
        total += first * second
print(total)