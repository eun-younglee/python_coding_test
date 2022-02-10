#코드트리 - Novice Mid - 시뮬레이션 2 - dx,dy 테크닉 - 되돌아오기 2

orders = input()
# N, E, S, W
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
face = 0
x, y = 0, 0
original = False
cnt = 0

for order in orders:
    if(order == 'R'):
        face = (face + 1) % 4
    elif(order == 'L'):
        face = (face - 1) % 4
    else: #order is F 
        x, y = x + dxs[face], y + dys[face]
    cnt += 1
    
    if(x == 0 and y == 0): # check if returned to original
        original = True
        print(cnt)
        break

if(original == False):
    print(-1)
