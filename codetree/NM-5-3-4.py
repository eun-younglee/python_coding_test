#코드트리 - Novice Mid - 시뮬레이션 2 - dx,dy 테크닉 - 작은 구슬의 이동

n, t = tuple(map(int, input().split()))
x, y, d = tuple(input().split())
# current location and direction facing
x, y = int(x) - 1, int(y) - 1
#     R, D, L, U
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

direction = {
    'R' : 0,
    'D' : 1,
    'L' : 2,
    'U' : 3
}

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

face = direction[d]
for _ in range(t):
    # see the next location
    nx, ny = x + dxs[face], y + dys[face]
    if(in_range(nx, ny)): #if in range
        x, y = nx, ny #change current coordinates
    else: #out of range
        face = (face + 4 - 2) % 4 #change direction you're facing 

print(x + 1, y + 1)
