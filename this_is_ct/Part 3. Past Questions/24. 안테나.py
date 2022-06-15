# 일직선상 마을에 여러 채의 집이 있고 특정 위치에 안테나 하나 설치
# 안테나로부터 모든 집까지의 거리의 총합이 최소가 되도록

n = int(input())
house = list(map(int, input().split()))
diff = []

house.sort()  # order house ascending order
result = house[len(house) // 2 - 1]
print(result)
