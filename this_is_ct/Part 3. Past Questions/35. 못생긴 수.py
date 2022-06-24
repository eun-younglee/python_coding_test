# 못생긴 수는 오직 2, 3, 5만 소인수로 가지는 수
# 1은 못생긴 수로 가정
# n번째 못생긴 수를 찾기

n = int(input())
dp = [0] * n
dp[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    # choose minimum from possible multiplication
    dp[i] = min(next2, next3, next5)
    if dp[i] == next2:  # minimum was next2
        i2 += 1  # increase index
        next2 = dp[i2] * 2  # multiply
    if dp[i] == next3:  # minimum was next3
        i3 += 1
        next3 = dp[i3] * 3
    if dp[i] == next5:  # minimum was next5
        i5 += 1
        next5 = dp[i5] * 5
print(dp[n - 1])
