# 코드트리 - Novice Mid - 시뮬레이션 2 - dx,dy 테크닉 - 방향에 맞춰 이동
n = int(input())
x, y = 0, 0
direc = {
    'W' : 0,
    'S' : 1,
    'N' : 2,
    'E' : 3
}
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
for i in range(n):
    az, time = input().split()
    time = int(time)
    x += dx[direc.get(az)] * time
    y += dy[direc.get(az)] * time
print(x, y)
