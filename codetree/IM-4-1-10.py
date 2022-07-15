# 코드트리 - Intermediate Mid - Greedy - Greedy - 폭탄 해체 작업

import heapq
n = int(input())
# (score, time limit)
bombs = [tuple(map(int, input().split())) for _ in range(n)]
answer = 0

times = [0 for _ in range(10001)]
bombs.sort(key=lambda x: -x[0])  # score descending

for score, time in bombs:
    for i in range(time, 0, -1):  # check all the times
        if times[i] == 0:  # empty time
            times[i] = 1  # disarm in that time
            answer += score
            break

print(answer)
