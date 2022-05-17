# 문자열을 1개 이상 단위로 잘라 압축하기
# 반복되는 문자열 패턴을 숫자+패턴 방식으로 표현
# 가장 짧은 문자열의 길이를 반환

def solution(s):
    answer = len(s)  # length before compression
    for i in range(1, len(s) // 2 + 1):  # cutting half is maximum division
        compressed = ""
        prev = s[:i]  # first pattern
        count = 1
        for j in range(i, len(s), i):  # check from after first pattern, by step
            if prev == s[j:j + i]:  # if next is the same as prev, increase count
                count += 1
            else:
                if count > 1:  # if there are more than one same pattern, put both number and pattern
                    compressed += str(count) + prev
                else:  # if there is only one pattern, put only pattern
                    compressed += prev
                prev = s[j:j + i]  # current pattern is now prev
                count = 1  # increase count
        # dealing with leftovers
        if count > 1:
            compressed += str(count) + prev
        else:
            compressed += prev
        answer = min(answer, len(compressed))  # find minimum length
    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
