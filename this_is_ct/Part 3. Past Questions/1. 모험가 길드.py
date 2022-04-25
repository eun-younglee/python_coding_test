# 공포도가 x인 모험가는 반드시 x 명 이상으로 구성해야 한다
# 몇 개의 모험가 그룹을 만들 수 있는지

n = int(input())
fear_level = list(map(int, input().split()))
group_number = 0

# order fear levels from large to small
fear_level.sort(reverse=True)
person = 0
while person < n:
    for i in range(fear_level[person]):
        person += 1
    group_number += 1

print(group_number)
