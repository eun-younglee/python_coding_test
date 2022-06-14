# 2 * 1 크기의 로봇을 움직여 (n, n) 위치로 이동하기
# (1, 1) 위치에서 가로 방향으로 놓여 있는 상태로 시작
# (n, n)까지 이동하는 데 걸리는 최소 시간

from collections import deque

board = [[0, 0, 0, 1, 1],
         [0, 0, 0, 1, 0],
         [0, 1, 0, 1, 1],
         [1, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]


def get_next_pos(pos, board):
    next_pos = []
    (x1, y1), (x2, y2) = pos
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    for dx, dy in zip(dxs, dys):
        nx1, ny1, nx2, ny2 = x1 + dx, y1 + dy, x2 + dx, y2 + dy
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            next_pos.append({(nx1, ny1), (nx2, ny2)})
    if x1 == x2:  # robot horizontally located
        for i in [-1, 1]:
            # if up or down empty
            if board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:
                next_pos.append({(x1, y1), (x1 + i, y1)})
                next_pos.append({(x2, y2), (x2 + i, y2)})
    elif y1 == y2:  # robot vertically located
        for i in [-1, 1]:
            # right or left empty
            if board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
                next_pos.append({(x1, y1), (x1, y1 + i)})
                next_pos.append({(x2, y2), (x2, y2 + i)})
    # return all possible next locations
    return next_pos


def solution(board):
    n = len(board)
    # fill borders with 1
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    q = deque()
    pos = {(1, 1), (1, 2)}
    visited = []
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        # arrived to (n, n)
        if (n, n) in pos:
            return cost
        # check possible locations from current location
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:  # add to queue if not visited
                visited.append(next_pos)
                q.append((next_pos, cost+1))


print(solution(board))
