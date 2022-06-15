# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨 있는 배열을 리턴

n = int(input())
answer = []
stages = [2, 1, 2, 6, 2, 4, 3, 3]
length = len(stages)
for i in range(1, n + 1):
    count = stages.count(i)  # count failure
    if length == 0:  # all stages counted
        fail = 0
    else:
        fail = count / length  # calculate failure percent
    answer.append((i, fail))  # append to the answer
    length -= count  # minus count

answer.sort(key=lambda x: (-x[1], x[0]))
answer = [i[0] for i in answer]
print(answer)
