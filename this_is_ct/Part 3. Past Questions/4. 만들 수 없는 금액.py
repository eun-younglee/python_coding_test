# n개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하기

n = int(input())
coins = list(map(int, input().split()))
coins.sort()
target = 1

for coin in coins:
    if target < coin:  # price that cannot be made
        break
    target += coin

print(target)
