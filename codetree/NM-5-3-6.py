#코드트리 - Novice Mid - 시뮬레이션 2 - dx,dy 테크닉 - 되돌아오기 

direction = {
    'N' : 0,
    'E' : 1,
    'S' : 2,
    'W' : 3
}
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
x, y = 0, 0
ans = -1
cnt = 0

def move(face, dist):
    global x, y
    global ans, cnt

    for _ in range(dist):
        x, y = x + dxs[face], y + dys[face]
        cnt += 1
        if(x == 0 and y == 0):
            ans = cnt
            return True
    return False 

n = int(input())
for _ in range(n):
    a, b = input().split()
    face = direction[a]
    b = int(b)

    moved = move(face, b)

    if moved:
        break

print(ans)
