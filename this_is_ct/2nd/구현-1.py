# Ch 4. - 실전문제 3. 게임 개발

# N * M의 직사각형에서 1은 바다고 0은 육지
# 캐릭터는 (A, B) 칸에서 북/동/남/서 방향을 바라보고 있
# 현재 위치에서 왼쪽부터 차례대로 갈 방향을 정하는데, 가보지 않은 칸이 있다면 돌아서 전진하고 가본 칸이라면 회전만 하는 것을 반복한다
# 네 방향 모두 가본 칸이거나 바다로 되어 있으면 한 칸 뒤로 가서 위의 방법을 반복한다
# 만약 뒤쪽 방향이 바다라면 움직임을 멈춘다

n, m = map(int, input().split())
x, y, head = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]  # N, W, S, E
visited[x][y] = True  # starting place visited
cnt = 1


def is_safe(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:  # out of range
        return False
    if graph[x][y] == 1:  # sea, can't go
        return False
    if visited[x][y]:  # visited
        return False
    return True


def all_four(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):  # check all four ways
        nx, ny = x + dx, y + dy
        if visited[nx][ny] is True or graph[nx][ny] == 1:
            cnt += 1
    if cnt == 4:
        return True
    return False


while True:
    if all_four(x, y):  # all four cannot go
        behind = (head + 2) % 4
        bx, by = x + dxs[behind], y + dys[behind]
        if graph[bx][by] == 1:  # behind is sea, break
            break
        else:
            x, y = bx, by
    head = (head + 1) % 4  # turn left
    nx, ny = x + dxs[head], y + dys[head]  # next place
    if is_safe(nx, ny):  # if safe, move
        x, y = nx, ny
        visited[nx][ny] = True
        cnt += 1


print(cnt)
