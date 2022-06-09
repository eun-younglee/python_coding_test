# n개의 수로 이루어진 수열과 n - 1 개의 연산자가 주어짐
# 숫자는 순서 바꿀 수 없어 연산자는 순서 바꿀 수 있음
# 연산자 우선순위 무시하고 처음부터 계산하기, 나눗셈은 정수 나눗셈
# 음수 나누기 양수는 양수로 바꾸고 몫을 음수로 바꾸기
# 만들 수 있는 식의 결과 최대와 최소 구하기
from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())  # number of each sign
signs = []
minimum, maximum = 1e9, -1e9


def dfs(i, now):
    global maximum, minimum, plus, minus, mul, div
    if i == n:
        minimum = min(minimum, now)
        maximum = max(maximum, now)
    else:
        if plus > 0:
            plus -= 1
            dfs(i + 1, now + numbers[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i + 1, now - numbers[i])
            minus += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / numbers[i]))
            div += 1


def calculate():
    maximum, minimum = -1e9, 1e9
    signs = ['+'] * plus
    signs.extend(['-'] * minus)
    signs.extend(['*'] * mul)
    signs.extend(['/'] * div)
    expression = list(permutations(signs, n - 1))
    for exp in expression:
        cal = numbers[0]
        for i in range(1, n):
            if exp[i - 1] == '+':
                cal += numbers[i]
            if exp[i - 1] == '-':
                cal -= numbers[i]
            if exp[i - 1] == '*':
                cal *= numbers[i]
            if exp[i - 1] == '/':
                cal = int(cal / numbers[i])
        maximum = max(maximum, cal)
        minimum = min(minimum, cal)
    return maximum, minimum


maax, miin = calculate()
print(maax, miin)
dfs(1, numbers[0])
print(maximum)
print(minimum)
