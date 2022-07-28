# 코드트리 - Intermediate Low - Simulation - 격자 안에서 터지고 떨어지는 경우 - 1차원 젠가 

n = int(input())
tower = []
for _ in range(n):
    tower.append(int(input()))  # from up to down
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())


def remove(s, e):
    add = -1
    for i in range(e, n):  # move to the front
        tower[s + add] = tower[i]
        add += 1
    for i in range(e - s + 1):  # delete leftover
        tower[n - (e - s + 1) + i] = -1


remove(s1, e1)
remove(s2, e2)

answer = []
for i in range(n):  # get only ones that are not -1
    if tower[i] != -1:
        answer.append(tower[i])

print(len(answer))
for i in range(len(answer)):
    print(answer[i])