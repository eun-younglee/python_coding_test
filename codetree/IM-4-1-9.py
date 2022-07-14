# 코드트리 - Intermediate Mid - Greedy - Greedy - 높은 숫자의 카드가 이기는 게임

n = int(input())
b_card = [int(input()) for _ in range(n)]
a_card = []
point = 0

# get a's card, it's ascending
for i in range(1, n * 2 + 1):
    if i not in b_card:
        a_card.append(i)

for b in b_card:
    removed = False
    for a in a_card:
        if a > b:  # larger than b's card
            a_card.remove(a)  # remove that card
            point += 1  # get point
            removed = True
            break
    if not removed:
        a_card.pop(0)  # none of the card larger, remove the smallest card

print(point)
