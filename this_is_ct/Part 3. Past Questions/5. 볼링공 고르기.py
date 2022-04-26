# n개의 무게가 적혀 있고 최대 무게가 m인
# 볼링공을 두 사람이 무게가 다르게 선택할 수 있는 조합의 경우의 수

n, m = map(int, input().split())
weight = list(map(int, input().split()))
result = 0

for one in range(n - 1):
    for two in range(one + 1, n):
        if weight[one] != weight[two]:
            result += 1
print(result)


array = [0] * 11
for w in weight:
    array[w] += 1  # count each weight

result = 0
for i in range(1, m + 1):
    n -= array[i]  # excluding number of balls that first person chooses
    result += array[i] * n  # multiply with second person choosing a ball
    # array[i] is first person choosing a ball * n is second person choosing a ball

print(result)
