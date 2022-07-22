# Ch 12 - 기출문제 7. 럭키 스트레이트

n = input()
first = n[:len(n) // 2]  # first half
second = n[len(n) // 2:]  # second half

first_sum, second_sum = 0, 0
for f, s in zip(first, second):
    first_sum += int(f)
    second_sum += int(s)

if first_sum == second_sum:
    print("LUCKY")
else:
    print("READY")
