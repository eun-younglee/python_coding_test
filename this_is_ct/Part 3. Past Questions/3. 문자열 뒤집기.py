# 0과 1로만 이루어진 문자열 s
# 연속된 하나 이상의 숫자를 잡고 모두 뒤집어 모두 같은 숫자로 바꾸기
def split(string):
    return [int(char) for char in string]


s = input()
s = split(s)
cnt0, cnt1 = 0, 0

if s[0] == 1:
    cnt0 += 1  # change to 0
else:
    cnt1 += 1  # change to 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:  # if two consecutive numbers are different
        if s[i + 1] == 1:  # change to 1
            cnt0 += 1
        else:  # change to 0
            cnt1 += 1

print(min(cnt0, cnt1))  # smaller one

