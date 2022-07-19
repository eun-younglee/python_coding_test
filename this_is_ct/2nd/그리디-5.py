# Ch 11 - 기출문제 3. 문자열 뒤집기
# 0과 1로만 이루어진 문자열 s에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집어 모두 같은 숫자로 바꿀 수 있는 최소 숫자

s = input()
cnt0, cnt1 = 0, 0

if s[0] == '0':  # first number is 0
    cnt1 += 1  # change to 1 
else:
    cnt0 += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i + 1] == '1':  # next number is 1
            cnt0 += 1  # change to 0
        else:  # next number is 0
            cnt1 += 1  # change to 1
print(min(cnt0, cnt1))
