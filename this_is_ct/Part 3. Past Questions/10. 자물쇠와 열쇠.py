# m * m 사이즈의 열쇠와 n * n 크기의 자물쇠가 있을 때
# 열쇠를 돌리거나 움직여 자물쇠의 모든 홈을 채워야 자물쇠를 열 수 있다
# 자물쇠를 열 수 있으면 true, 열 수 없으면 false

def check(new_lock):
    length = len(new_lock) // 3  # check the middle
    for i in range(length, length * 2):
        for j in range(length, length * 2):
            if new_lock[i][j] != 1:  # False if it's number other than 1
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # expand lock to three times the original
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # copy original lock to new lock
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # for 4 directions
    for _ in range(4):
        key = list(zip(*key))[::-1]
        # key starts from (x, y)
        for x in range(n * 2):
            for y in range(n * 2):
                # get the key range
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock) is True:  # if every number within a range is 1, can unlock
                    return True
                # cannot unlock, return to original lock status
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False


key = [[0, 0, 0],
       [1, 0, 0],
       [0, 1, 1]]
lock = [[1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]]

if solution(key, lock) is True:
    print("true")
else:
    print("false")
