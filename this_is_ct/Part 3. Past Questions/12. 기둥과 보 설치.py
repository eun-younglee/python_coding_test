# 기둥은 바닥 위에 있거나 보의 한쪽 끝부분 위에 이써가 다른 기둥 위에 있어야
# 보는 한쪽 끝부분이 기둥 위에 있거나 양쪽 끝부분이 다른 보와 동시에 연결되어야
# [x, y, a, b]에서 x, y는 기둥이나 보를 설치할 가로, 세로 좌표
# a는 0이 기둥, 1이 보 / b는 0이 삭제, 1이 설치
# 조건을 만족하지 않는 작업은 무시한 후 최종 구조물의 상태를 리턴

n = int(input())  # grid
# build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1],
#                [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1],
               [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]


def is_safe(result):
    for x, y, a in result:
        if a == 0:
            if y == 0 or [x, y - 1, 0] in result or [x - 1, y, 1] in result or [x, y, 1] in result:
                continue
            return False
        else:
            if [x, y - 1, 0] in result or [x + 1, y - 1, 0] in result or \
                    ([x - 1, y, 1] in result and [x + 1, y, 1] in result):
                continue
            return False
    return True


result = []
for build in build_frame:
    x, y = build[0], build[1]
    a, b = build[2], build[3]
    if b == 0:  # remove
        result.remove([x, y, a])
        if not is_safe(result):  # cannot remove, install again
            result.append([x, y, a])
    else:  # install
        result.append([x, y, a])
        if not is_safe(result):  # cannot install, remove
            result.remove([x, y, a])


result.sort()
print(result)
