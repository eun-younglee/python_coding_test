# 코드트리 - Novice Mid - 시뮬레이션 2 - dx,dy 테크닉 - 문자에 따른 명령 2
go = input()
# N, E, S, W
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0
face = 0
# L이면 -1, R이면 +1
for g in go:
    if(g == "L"):
        face = (face - 1 + 4) % 4
    elif(g == "R"):
        face = (face + 1) % 4
    else: # go forward
        x += dx[face]
        y += dy[face]
print(x, y)
