# 코드트리 - Intermediate Mid - Greedy - Greedy - 회의실 겹치지 않게 하기

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: x[1])  # early ending first

ending = -1
delete = 0
for s, e in meetings:
    if s >= ending:  # next meeting possible
        ending = e
    else:  # next meeting not possible
        delete += 1  # count the cases
print(delete)
