# 숫자 카드 게임

n, m = map(int, input().split())
cards = [
    list(map(int, input().split()))
    for _ in range(n)
]

mins = []
for i in range(n):
    mins.append(min(cards[i]))  # find the smallest numbers on each rwo
print(max(mins))
