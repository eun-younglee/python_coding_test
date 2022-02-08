# 코드트리 - Novice Mid - 시뮬레이션 2 - dx,dy 테크닉 - 1이 3개 이상 있는 위치

n = int(input())
matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]

#격자에서의 x, y
#      E, S, W, N
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def check_one(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if(in_range(nx, ny) and matrix[nx][ny] == 1):
            cnt += 1
    return cnt 

ones = 0
total = 0
for x in range(n):
    for y in range(n):
        ones = check_one(x, y)
        if(ones >= 3):
            total += 1
print(total)
