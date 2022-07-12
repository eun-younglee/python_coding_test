# 코드트리 - IntermediateMid - Greedy - Greedy - 최대 숫자 만들기

from functools import cmp_to_key


def compare(x, y):
    xy = x + y
    yx = y + x
    if int(xy) > int(yx):
        return -1
    else:
        return 1
    return 0


n = int(input())
numbers = [input() for _ in range(n)]
numbers.sort(key=cmp_to_key(compare))
for number in numbers:
    print(number, end="")
