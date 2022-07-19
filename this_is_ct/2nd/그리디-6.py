# Ch 11 - 기출문제 4. 만들 수 없는 금액
# n개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하기

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for coin in coins:
    if target < coin:
        print(target)
        break
    target += coin
