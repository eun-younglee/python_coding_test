# 두 배열의 원소 교체

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a should be ordered from small to large
# b should be ordered from large to small

a = sorted(a)
b = sorted(b, reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
