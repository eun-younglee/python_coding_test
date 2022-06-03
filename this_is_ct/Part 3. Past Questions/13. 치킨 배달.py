# 크기가 n * n인 도시가 있고 각 칸은 빈칸, 치킨집, 집 중 하나
# 치킨거리: 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리: 모든 집의 치킨 거리의 합
# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜 도시의 치킨 거리 가장 작게 만들기
from itertools import combinations

n, m = map(int, input().split())
#city_map = [list(map(int, input().split())) for _ in range(n)]
#city_map = [[0, 0, 1, 0, 0], [0, 0, 2, 0, 1], [0, 1, 2, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 2]]
#city_map = [[0, 2, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0], [2, 0, 0, 1, 1], [2, 2, 0, 1, 2]]
city_map = [[1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0]]
chicken, house = [], []


# find location of chicken restaurants
def find_loc():
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 2:  # is a chicken restaurant
                chicken.append([i, j])
            if city_map[i][j] == 1:  # is a house
                house.append([i, j])


def chicken_distance(save):
    city_chicken_dist = 0
    for h in house:
        min_dist = 1e9
        for s in save:
            hx, hy = h
            sx, sy = s
            min_dist = min(min_dist, abs(hx - sx) + abs(hy - sy))  # calculate chicken distance
        city_chicken_dist += min_dist
    return city_chicken_dist


find_loc()
saves = list(combinations(chicken, m))  # combination of chicken restaurants

min_distance = 10000
for save in saves:  # check all combinations
    distance = chicken_distance(save)
    min_distance = min(distance, min_distance)
print(min_distance)
