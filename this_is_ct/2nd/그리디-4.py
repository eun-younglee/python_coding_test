# Ch 11 - 기출문제 2. 곱하기 혹은 더하기
# 0 ~ 9의 숫자로 이루어진 문자열 s 가 주어짐
# 왼쪽부터 오른쪽으로 가며 숫자 하나하나 확인
# 숫자 사이에 x 혹은 + 연산을 넣어 결과적으로 만들어질 수 있는 가장 큰 수 구하기

s = list(input())
result = int(s[0])
for i in range(1, len(s)):
    number = int(s[i])
    if result <= 1 or number <= 1:
        result += number
    else:
        result *= number
print(result)
