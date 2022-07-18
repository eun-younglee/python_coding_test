# 코드트리 - Intermediate Mid - Greedy - Greedy - 적석과 흑석

c, n = map(int, input().split())  # red, black
reds = [int(input()) for _ in range(c)]
blacks = [list(map(int, input().split())) for _ in range(n)]

reds.sort()
blacks.sort()

cnt = 0
for i in range(c - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if blacks[j][0] <= reds[i] <= blacks[j][1]:  # within range
            blacks[j][0], blacks[j][1] = -1, -1  # used
            cnt += 1
            break

print(cnt)
