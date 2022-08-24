# Ch 13 - 기출문제 20. 감시 피하기
#
# n * n 크기의 복도
# 선생님이 상하좌우 방향으로 감시하며 장애물이 있으면 뒤에 있는 학생은 볼 수 없음
# 선생님은 t, 학생은 s, 장애물은 o
# 장애물을 3개 설치하여 모든 학생이 선생님의 감시를 피할 수 있는지 출력 - YES / NO

from itertools import combinations
import copy

n = int(input())
graph = []
teachers, empty = [], []
for i in range(n):
    line = list(input().split())
    for j in range(n):
        if line[j] == 'X':  # empty locations
            empty.append([i, j])
        if line[j] == 'T':  # teacher locations
            teachers.append([i, j])


def check_teacher(graph_new, teacher):
    pass


def surveillance(graph_new):
    for teacher in teachers:
        if check_teacher(graph_new, teacher) is True:  # student found, return false
            return False
    return True  # all student safe


can_escape = False
obstacles = list(combinations(empty, 3))  # get three obstacles
for obstacle in obstacles:
    # install obstacle
    graph_new = copy.deepcopy(graph)
    if surveillance(graph_new):  # check if everyone escapes surveillance
        can_escape = True
        break
if can_escape:
    print("YES")
else:
    print("NO")