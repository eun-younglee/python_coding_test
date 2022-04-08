# 효율적인 화폐 구성

n, m = map(int, input().split())
money = [int(input()) for i in range(n)]
dp = [10000] * (m + 1)

# initialise
dp[0] = 0
for mo in money:
    if mo < (m + 1):
        dp[mo] = 1

# calculate dp
for i in range(3, m + 1):
    for mo in money:
        if i - mo > 0 and dp[i - mo] != 10000:
            dp[i] = min(dp[i], dp[i - mo] + 1)

print(dp)
if dp[m] == 10000:
    print(-1)
else:
    print(dp[m])
