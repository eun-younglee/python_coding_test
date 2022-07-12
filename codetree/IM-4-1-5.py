# 코드트리 - IntermediateMid - Greedy - Greedy - 회의실 준비 구현

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort(key = lambda x: x[1])
cnt = 1
end = meetings[0][1]

for i in range(1, n):
    next_start = meetings[i][0]
    if next_start >= end:  # no overlapping, choose
        cnt += 1
        end = next_start  # change
print(cnt)
