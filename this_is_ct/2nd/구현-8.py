# Ch 12 - 기출문제 13. 치킨 배달
#
# 크기가 n * n인 도시가 있고 각 칸은 빈칸, 치킨집, 집 중 하나
# 치킨거리: 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리: 모든 집의 치킨 거리의 합
# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜 도시의 치킨 거리 가장 작게 만들기
from itertools import combinations
import sys

n, m = map(int, input().split())
chicken, house = [], []
graph = []
for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(n):
        if line[j] == 2:  # get chicken location
            chicken.append([i, j])
        if line[j] == 1:  # get house location
            house.append([i, j])

min_dist = sys.maxsize
chi_comb = list(combinations(chicken, m))  # combination of chicken restaurants
for comb in chi_comb:
    chicken_dist = 0
    for hs_x, hs_y in house:
        min_house = sys.maxsize
        for chi_x, chi_y in comb:
            dist = abs(hs_x - chi_x) + abs(hs_y - chi_y)  # get distance
            min_house = min(dist, min_house)  # get minimum distance by each house
        chicken_dist += min_house  # sum
    min_dist = min(min_dist, chicken_dist)  # get smallest chicken distance

print(min_dist)
