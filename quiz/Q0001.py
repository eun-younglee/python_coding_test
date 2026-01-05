# Q0001: Palindrome Number
# 📋 문제 설명
# 정수 x가 주어집니다. x가 회문(palindrome)인지 판별하세요.

# 회문이란 앞에서 읽으나 뒤에서 읽으나 같은 숫자를 말합니다.

# 입력
# x: number    // 정수

# 제약사항
# -2^31 <= x <= 2^31 - 1

# 힌트
# 음수는 회문이 될 수 없습니다
# 숫자를 문자열로 변환하지 않고도 풀 수 있습니다


def solve(x):
  if x < 0 or x % 10 == 0:
    return False

  x_reverse = 0

  while (x > x_reverse):
    x_reverse = x_reverse * 10 + x % 10
    x = x // 10
    # print("x: ", x, "reverse: ", x_reverse);
  
  if (x == x_reverse) or (x == x_reverse // 10): 
    return True
  return False

print(solve(101))  # True
print(solve(100))  # False
print(solve(100001))  # True
print(solve(-1234))  # False
print(solve(10000000000000000000001))  # True 