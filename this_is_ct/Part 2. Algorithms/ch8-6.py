# 개미 전사

n = int(input())
food = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = food[0]
dp[1] = max(food[0], food[1])
for i in range(n):
    dp[i] = max(dp[i - 2] + food[i], dp[i - 1])

print(dp[n - 1])