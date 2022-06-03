# 동그란 모양이고 외벽의 둘레는 n 미터
# 사람 별 1시간 동안 이동할 수 있는 거리가 제공되었을 때
# 시계 혹은 반시계 방향으로 외벽을 따라 움직여
# 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최솟값
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)  # expend the weak
    answer = len(dist) + 1  # initialisation
    for start in range(length):
        # check every permutation
        for friends in list(permutations(dist, len(dist))):
            count = 1
            # last position for the friend to check
            position = weak[start] + friends[count - 1]
            # check all weak points
            for index in range(start, start + length):
                # out of distance
                if position < weak[index]:
                    count += 1  # add a friend
                    if count > len(dist):  # end if friend count exceed number of friends
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
        if answer > len(dist):
            return -1
    return answer

n = int(input())
# weak = list(map(int, input().split()))
# dist = list(map(int, input().split()))
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
answer = solution(n, weak, dist)
print(answer)
