# Ch 11 - 기출문제 1. 모험가 길드
# 공포도가 x인 모험가는 반드시 x 명 이상으로 구성해야 할 때 몇 개의 모험가 그룹을 만들 수 있는지

n = int(input())
frights = list(map(int, input().split()))
frights.sort(reverse=True)  # order descending
answer = 0

while True:
    first = frights[0]
    if first > len(frights):  # cannot form anymore groups
        break
    if first == len(frights):
        answer += 1
        break
    for i in range(first):  # according to most frightened member
        frights.pop(0)  # member disposed
    answer += 1  # one group formed

print(answer)
