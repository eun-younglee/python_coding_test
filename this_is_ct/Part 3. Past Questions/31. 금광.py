# n * m 크기의 금광에서 금을 캘 때 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 위치로 이동 가능
# 채굴자가 얻을 수 있는 금의 최대 크기 출력
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
n, m = map(int, input().split())
array = list(map(int, input().split()))
mine, dp = [], [[0] * m for _ in range(n + 2)]
for i in range(1, n + 1):
    mine.append(array[m * (i - 1): m * i])

for i in range(1, n + 1):
    dp[i][0] = mine[i - 1][0]

for j in range(1, m):
    for i in range(1, n + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1], dp[i + 1][j - 1]) + mine[i - 1][j]

maximum = -1e9
for i in range(1, n + 1):
    maximum = max(maximum, dp[i][m - 1])
print(maximum)
