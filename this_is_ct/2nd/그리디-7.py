# Ch 11 - 기출문제 5. 볼링공 고르기
# n개의 무게가 적혀 있고 최대 무게가 m인 볼링공을 두 사람이 무게가 다르게 선택할 수 있는 조합의 경우의 수

n, m = map(int, input().split())
weight = list(map(int, input().split()))
balls = [0] * (m + 1)
for w in weight:
    balls[w] += 1  # count balls in each weight

result = 0
for i in range(1, m + 1):
    n -= balls[i]  # first person chooses
    result += balls[i] * n  # first person choose * second person choose
print(result)
