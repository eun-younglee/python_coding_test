# 코드트리 - Novice Mid - 시뮬레이션 2 - dx,dy 테크닉 - 빙빙 돌며 숫자 사각형 채우기 

n, m = tuple(map(int, input().split()))
matrix = [[0 for _ in range(m)] for _ in range(n)]
x, y = 0, 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

face = 0
matrix[0][0] = 1
for i in range(2, n * m + 1):
    while True:
        nx, ny = x + dx[face], y + dy[face]
        if(in_range(nx, ny) and matrix[nx][ny] == 0): 
            x, y = nx, ny
            matrix[x][y] = i
            break
        else:
            face = (face + 1) % 4

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end = " ")
    print()
