# 코드트리 - IntermediateMid - Greedy - Greedy - 자동차 단일 거래 이익 최대화하기 2

n = int(input())
price = list(map(int, input().split()))

max_profit = 0
min_price = price[0]
for i in range(n):
    profit = price[i] - min_price
    max_profit = max(max_profit, profit)
    min_price = min(min_price, price[i])
print(max_profit)
