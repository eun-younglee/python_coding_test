# 오늘부터 n + 1 되는 날 퇴사하기 위해 남은 n일 동안 최대한 많은 상담 하기
# 상담을 완료하는 데 걸리는 기간 t와 상담을 했을 때 받을 수 있는 금액 p

n = int(input())
t, p = [], []
for _ in range(n):
    time, pay = map(int, input().split())
    t.append(time)
    p.append(pay)

dp = [0] * (n + 1)  # dp[i] is max profit from day i to the end
max_value = 0
for i in range(n - 1, -1, -1):
    time = i + t[i]  # current date + period needed for consulting
    if time <= n:  # not exceeding quitting date
        dp[i] = max(p[i] + dp[time], max_value)  # current pay + max profit from the day current consulting ended
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)
