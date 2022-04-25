# 바닥 공사

n = int(input())
dp = [0] * (n + 1)

# initialise
dp[1] = 1
dp[2] = 3

# calculate dp
for i in range(3, n + 1):
    dp[i] = (dp[i - 2] * 2 + dp[i - 1]) % 796796
print(dp[n])
