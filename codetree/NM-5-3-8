#코드트리 - Novice Mid - 시뮬레이션 2 - dx,dy 테크닉 - 격자 위의 편안한 상태 

n, m = map(int, input().split())
matrix = [[0 for _ in range(n)] for _ in range(n)]
# have to check if you're on comfort zone every time
#     N, E, S, W
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def check_adjacent(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys): #check all the spots
        #see if it's coloured
        nx, ny = x + dx, y + dy
        if(in_range(nx, ny) and matrix[nx][ny] == 1):
            cnt += 1
    return cnt 

for _ in range(m):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1
    colour = 0
    matrix[r][c] = 1 #colour the current spot
    
    if(check_adjacent(r, c) == 3): #comfort zone
        print(1)
    else: #not comfort zone
        print(0)
