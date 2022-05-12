# 알파벳 대문자와 숫자로 구성된 문자열 주어짐
# 알파벳을 오름차순으로 정렬하여 출력하고 모든 숫자를 더한 값 출력
# K1KA5CB7
s = input()
alp = list()
num = list()

for char in s:
    if char.isnumeric():  # is number
        num.append(int(char))
    else:  # is alphabet
        alp.append(char)

alp.sort()  # order alphabetically
result = ''.join(str(i) for i in alp)  # list to string
print(result + str(sum(num)))
