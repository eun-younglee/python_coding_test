# 코드트리 - Intermediate Low - Simulation - 격자 안에서 밀고 당기기 - 컨베이어 벨드

n, t = map(int, input().split())
upper = list(map(int, input().split()))
under = list(map(int, input().split()))

# upper right to under right
# under right to upper right
for _ in range(t):
    temp_upper = upper[n - 1]
    temp_under = under[n - 1]
    for i in range(n - 2, -1, -1):  # pushing to the right
        upper[i + 1] = upper[i]
        under[i + 1] = under[i]
    under[0] = temp_upper
    upper[0] = temp_under

for i in range(n):
    print(upper[i], end=" ")
print()
for i in range(n):
    print(under[i], end=" ")
