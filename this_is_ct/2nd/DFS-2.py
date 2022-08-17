# Ch 13 - 기출문제 18. 괄호 변환
#
# 괄호의 (와 ) 개수가 같으면 균형잡힌 괄호 문자열
# () 짝이 모두 맞으면 올바른 괄호 문자열
# 문자열을 균형잡힌 괄호 문자열 u, v로 분리
# u는 균형잡힌 괄호 문자열로 더 이상 분리 불가, v는 빈 문자열 가능
# 문자열 u가 올바르면 v에 대해서 처음부터 시행
# u가 올바르지 않으면 빈 문자열에 첫번째 문자로 (를 붙이고
# v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 붙이고 )를 다시 붙임
# u의 첫 번쨰와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향 뒤집기


def right_str(p):
    cnt = 0  # left bracket count
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True  # right sets


def balanced_str(p):
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == "(":
            left += 1
        else:
            right += 1
        if left == right:
            return i
    return i


def reverse(p):
    temp = ""
    for i in range(len(p)):
        if p[i] == "(":
            temp += ")"
        else:
            temp += "("
    return temp


def solution(p):
    answer = ""
    if p == "":
        return answer
    left, right = 0, 0
    index = balanced_str(p)
    u, v = p[:index + 1], p[index + 1:]
    if right_str(u):  # u is right
        answer = u + solution(v)
    else:  # u is not right
        temp = solution(v)  # recursion on p
        answer = "(" + temp + ")" + reverse(list(u[1:-1]))
    return answer


print(solution("()))((()"))
print()
print(solution(")("))