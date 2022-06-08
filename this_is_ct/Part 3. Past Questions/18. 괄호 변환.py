# 괄호의 (와 ) 개수가 같으면 균형잡힌 괄호 문자열
# () 짝이 모두 맞으면 올바른 괄호 문자열
# 문자열을 균형잡힌 괄호 문자열 u, v로 분리
# u는 균형잡힌 괄호 문자열로 더 이상 분리 불가, v는 빈 문자열 가능
# 문자열  u가 올바르면 v에 대해서 처음부터 시행
# u가 올바르지 않으면 빈 문자열에 첫번째 문자로 (를 붙이고
# v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 붙이고 )를 다시 붙임
# u의 첫 번쨰와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향 뒤집기
from collections import deque


def is_balanced(w):  # check if the no. of left and right are the same
    left, right = 0, 0
    for i in range(len(w)):
        if w[i] == '(':
            left += 1
        else:
            right += 1
    return left == right


def is_correct(w):  # check if pairs are right
    q = deque()
    for i in range(len(w)):
        letter = w[i]
        if letter == "(":
            q.append(letter)
        else:
            if len(q) == 0:  # queue empty before checking all the string
                return False  # not matched
            else:
                q.pop()  # found pairs
    return len(q) == 0  # if there are leftover, it's not balanced


def change(w):
    u, v, answer = "", "", ""
    if is_correct(w) or len(w) == 0:
        return w
    for i in range(2, len(w) + 1, 2):  # find u and v
        u, v = w[:i], w[i:]
        if is_balanced(u):  # u if balanced
            break
    if is_correct(u):
        answer += u + change(v)
    else:
        answer += "(" + change(v) + ")"
        u = u[1:-1]
        for c in u:
            if c == "(":
                answer += ")"
            else:
                answer += "("
    return answer


print(change("(()())()"))
print(change(")("))
print(change("()))((()"))
