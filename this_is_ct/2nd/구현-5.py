# Ch 12 - 기출문제 10. 자물쇠와 열쇠

# m * m 사이즈의 열쇠와 n * n 크기의 자물쇠가 있을 때
# 열쇠를 돌리거나 움직여 자물쇠의 모든 홈을 채워야 자물쇠를 열 수 있다
# 자물쇠를 열 수 있으면 true, 열 수 없으면 false


def check(graph, n):
    for i in range(n - 1, 2 * n - 1):
        for j in range(n - 1, 2 * n - 1):
            if graph[i][j] != 1:  # have zero, false
                return False
    return True  # all 1


def solution(key, lock):
    m, n = len(key), len(lock)
    graph = [[0] * (n * 3 - 2) for _ in range(n * 3 - 2)]  # expand lock
    length = len(graph)
    for i in range(n):  # copy lock
        for j in range(n):
            graph[i + n - 1][j + n - 1] = lock[i][j]
    # try all four direction
    for _ in range(4):
        key = list(zip(*key[::-1]))  # turn the key
        for i in range(length - n + 1):
            for j in range(length - n + 1):
                for x in range(m):
                    for y in range(m):
                        graph[x + i][y + j] += key[x][y]  # put key to the lock
                result = check(graph, n)  # check if key fits into lock
                if result is True:
                    return True
                # key doesn't fit, reset the lock
                for x in range(m):
                    for y in range(m):
                        graph[x + i][y + j] -= key[x][y]  # minus the key

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