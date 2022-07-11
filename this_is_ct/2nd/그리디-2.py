# Ch 3 - 실전문제 - 4. 1이 될 때까지
# 숫자 n과 k가 주어진다.
# n이 1이 될 때까지 n에서 1을 빼거나 n을 k로 나누는 과정을 반복한다. n을 k로 나누는 것은 나누어 떨어질 때만 가능하다.

n, k = map(int, input().split())
cnt = 0
while True:
    if n < k:
        break
    if n % k > 0:  # minus
        cnt += n % k
        n -= n % k
    n //= k
    cnt += 1

print(int(cnt) + (n % k - 1))
