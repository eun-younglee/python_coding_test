# Ch 12 - 기출문제 9. 문자열 압축

s = input()
length = 1000

for i in range(1, len(s) // 2 + 1):  # try until cutting in half
    result = ""
    pattern = s[:i]
    cnt = 1  # same pattern count
    for j in range(i, len(s), i):
        if pattern == s[j:j + i]:  # matching pattern
            cnt += 1  # increase count
        else:
            if cnt > 1:  # if count is over 1
                result += str(cnt)  # add pattern count to result
            result += pattern  # add pattern to result
            cnt = 1  # reset count
            pattern = s[j:j + i]  # new pattern as current letters
    # append leftover letters
    if cnt > 1:
        result += str(cnt)
    result += pattern
    length = min(length, len(result))  # find minimum length
print(length)
