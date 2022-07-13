# 코드트리 - IntermediateMid - Greedy - Greedy - 수 채우기

n = int(input())
can_fill = False

five = n // 5  # maximum number of five cent coin
for i in range(five, -1, -1):  # try all possible five coins
    cnt = 0
    cnt += i  # five cent coin count
    money = n - 5 * i  # minus the price
    if money % 2 == 0:  # if can divide by two cent coin
        cnt += money // 2  # two cent coin count
        can_fill = True  # can be filled
        break

if can_fill:
    print(cnt)
else:
    print(-1)
