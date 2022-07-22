# Ch 12 - 기출문제 8. 문자열 재정렬

s = input()
alphabet = []
number = []

for letter in s:
    if letter.isnumeric():  # is number
        number.append(int(letter))  # switch to numeric
    else:  # is alphabet
        alphabet.append(letter)

alphabet.sort()  # alphabetical order
result = "".join(map(str, alphabet))  # add to result
result += str(sum(number))  # add to result
print(result)
