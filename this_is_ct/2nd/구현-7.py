# Ch 12 - 기출문제 12. 기둥과 보 설치
#
# 기둥은 바닥 위에 있거나 보의 한쪽 끝부분 위에 있거나 다른 기둥 위에 있어야
# 보는 한쪽 끝부분이 기둥 위에 있거나 양쪽 끝부분이 다른 보와 동시에 연결되어야
# [x, y, a, b]에서 x, y는 기둥이나 보를 설치할 가로, 세로 좌표
# a는 0이 기둥, 1이 보 / b는 0이 삭제, 1이 설치
# 조건을 만족하지 않는 작업은 무시한 후 최종 구조물의 상태를 리턴

n = int(input())
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1],
               [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]


def is_safe(answer):
    okay = 0
    for x, y, a in answer:
        if a == 0:  # vertical
            if y == 0:  # under is ground
                okay += 1
            else:  # under is another pillar or bridge
                if [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
                    okay += 1
        else:  # horizontal
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer:  # on a pillar
                okay += 1
            elif [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:  # both ways connected
                okay += 1
    if okay == len(answer):  # all safe
        return True
    else:
        return False


def solution(build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 0:  # delete
            answer.remove([x, y, a])
            if not is_safe(answer):  # not safe, put back again
                answer.append([x, y, a])
        else:  # build
            answer.append([x, y, a])
            if not is_safe(answer):  # not safe, remove
                answer.remove([x, y, a])
    return answer


answer = solution(build_frame)
print(sorted(answer))
