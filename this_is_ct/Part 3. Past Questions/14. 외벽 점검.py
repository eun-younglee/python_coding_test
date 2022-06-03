# 동그란 모양이고 외벽의 둘레는 n 미터
# 사람 별 1시간 동안 이동할 수 있는 거리가 제공되었을 때
# 시계 혹은 반시계 방향으로 외벽을 따라 움직여
# 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최솟값

n = int(input())
# weak = list(map(int, input().split()))
# dist = list(map(int, input().split()))
# weak = [1, 5, 6, 10]
# dist = [1, 2, 3, 4]
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
dist_dist = []
for i in range(len(weak) - 1, -1, - 1):
    dist_dist.append((weak[i] - weak[i - 1] + n) % n)
print(dist_dist)

if max(dist) >= sum(dist_dist) - max(dist_dist):  # can be done by one person
    print(1)

