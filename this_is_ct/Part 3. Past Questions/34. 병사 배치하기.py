# n명의 병사가 무잠ㄱ위로 나열되어 있고 특정 값 전투력 보유
# 전투력 높은 병사가 앞에 오도록 내림차순 배치
# 특정 위치 병사를 열외시키고 남아있는 병사 최대가 되도록

n = int(input())
soldiers = list(map(int, input().split()))

# longest increasing partial array
dp = [1] * n
for i in range(n):
    for j in range(i):
        if soldiers[j] > soldiers[i]:  # in descending order
            dp[i] = max(dp[i], dp[j] + 1) 

print(n - max(dp))
