# 코드트리 - Intermediate Low - Simulation - 격자 안에서 터지고 떨어지는 경우 - 1차원 폭발 게임 - 내가 푼 버젼

n, m = map(int, input().split())
bombs = []
for _ in range(n):  # up to down
    bombs.append(int(input()))


def explosion(explode):
    for prev_index, cnt in explode:
        for i in range(cnt):
            bombs[prev_index + i] = 0  # make to 0
    for i in range(len(bombs) - 1, -1, -1):  # get rid of 0
        if bombs[i] == 0:
            bombs.pop(i)


while True:
    if len(bombs) == 0:  # no more bombs left
        break

    explode, did_explode = [], False
    prev, prev_index = bombs[0], 0
    cnt = 1
    for i in range(1, len(bombs)):
        if prev == bombs[i]:  # same as before
            cnt += 1
        if prev != bombs[i]:  # not same as before
            if cnt >= m:  # explode
                explode.append([prev_index, cnt])
                did_explode = True
            cnt = 1  # update
            prev, prev_index = bombs[i], i  # update
    if cnt >= m:  # deal with leftover
        explode.append([prev_index, cnt])
        did_explode = True
    if did_explode is False:  # no more left to explode
        break
    explosion(explode)

print(len(bombs))
for i in range(len(bombs)):
    print(bombs[i])