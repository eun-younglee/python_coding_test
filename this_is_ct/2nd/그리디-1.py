# Ch 3 - 실전문제 - 2. 큰 수의 법칙
# 주어진 수들은 M번 더하여 가장 큰 수 만들기.
# 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과해서 더해질 수 없음.
# 그리디 방식으로 풀기.

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)  # big number first
answer = 0
answer += numbers[0] * m // (k + 1) * k  # first number
answer += numbers[1] * m // (k + 1)  # second number
answer += numbers[0] * m % (k + 1)  # first number
print(answer)
