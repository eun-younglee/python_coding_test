# 1이 될 때까지

n, k = map(int, input().split())
cnt = 0
while True:
    if n < k:
        break
    cnt += n % k  # subtracting until dividable number
    n -= (n % k)
    n //= k  # divide
    cnt += 1

print(cnt + (n % k - 1))  # subtract leftovers
