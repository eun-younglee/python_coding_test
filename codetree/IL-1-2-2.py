# 코드트리 - Intermediate Low - Simulation - 격자 안에서 밀고 당기기 - 삼각형 컨베이어 벨드

n, t = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))

# last element to first
for _ in range(t):
    temp_first = first[n - 1]
    temp_second = second[n - 1]
    temp_third = third[n - 1]
    for i in range(n - 1, 0, -1):  # push to the right
        first[i] = first[i - 1]
        second[i] = second[i - 1]
        third[i] = third[i - 1]
    second[0] = temp_first
    third[0] = temp_second
    first[0] = temp_third

for i in range(n):
    print(first[i], end=" ")
print()
for i in range(n):
    print(second[i], end=" ")
print()
for i in range(n):
    print(third[i], end=" ")