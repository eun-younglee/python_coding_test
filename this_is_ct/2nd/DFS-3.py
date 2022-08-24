# Ch 13 - 기출문제 19. 연산자 끼워 넣기

# n개의 수로 이루어진 수열과 n - 1 개의 연산자가 주어짐
# 숫자는 순서 바꿀 수 없어 연산자는 순서 바꿀 수 있음
# 연산자 우선순위 무시하고 처음부터 계산하기, 나눗셈은 정수 나눗셈
# 음수 나누기 양수는 양수로 바꾸고 몫을 음수로 바꾸기
# 만들 수 있는 식의 결과 최대와 최소 구하기
import sys
from itertools import permutations

n = int(input())
a = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())
max_result, min_result = -sys.maxsize, sys.maxsize
signs = []


def calculate(sign):
    ans = a[0]
    cnt = 0
    for i in range(1, n):
        if sign[cnt] == '+':
            ans = ans + a[i]
        if sign[cnt] == '-':
            ans = ans - a[i]
        if sign[cnt] == '*':
            ans = ans * a[i]
        if sign[cnt] == '/':
            ans = int(ans / a[i])
        cnt += 1
    return ans


signs.extend(["+"] * plus)
signs.extend(["-"] * minus)
signs.extend(["*"] * multiply)
signs.extend(["/"] * divide)

signs_comb = list(permutations(signs, n - 1))
for sign in signs_comb:  # try all permutations
    result = calculate(sign)
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)
