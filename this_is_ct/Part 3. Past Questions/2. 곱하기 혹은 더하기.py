# 0 ~ 9의 숫자로 이루어진 문자열 s 가 주어짐
# 왼쪽부터 오른쪽으로 가며 숫자 하나하나 확인
# 숫자 사이에 x 혹은 + 연산을 넣어 결과적으로 만들어질 수 있는 가장 큰 수

s = input()
result = int(s[0])  # first number

for i in range(1, len(s)):
    num = int(s[i])
    if num <= 1 or result <= 1:  # add if smaller than 1
        result += num
    else:  # multiply
        result *= num

print(result)
