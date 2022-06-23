# 정수가 있는 삼각형에서 맨 위층부터 아래로 내려오며 수 하나를 선택할 때 합이 최대가 되도록


n = int(input())
triangle = [[0] * n for _ in range(n)]
for i in range(n):  # put triangle into matrix
    numbers = list(map(int, input().split()))
    j = i
    for num in numbers:
        triangle[j][i - j] = num
        j -= 1

dp = [[0] * n for _ in range(n)]
dp[0][0] = triangle[0][0]
for i in range(1, n):  # initialise
    dp[0][i] = dp[0][i - 1] + triangle[0][i]
    dp[i][0] = dp[i - 1][0] + triangle[i][0]
# only down or right is possible
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + triangle[i][j]
print(dp[n - 1][n - 1])
