# 코드트리 - Intermediate Low - Simulation - 격자 안에서 터지고 떨어지는 경우 - 1차원 폭발 게임 - 답안

n, m = tuple(map(int, input().split()))
numbers = []
for _ in range(n):
    numbers.append(int(input()))


def get_end_idx_of_explosion(start_idx, curr_num):
    for end_idx in range(start_idx + 1, len(numbers)):
        if numbers[end_idx] != curr_num:
            return end_idx - 1

    return len(numbers) - 1


while True:
    did_explode = False

    for curr_idx, number in enumerate(numbers):
        if number == 0:  # ignore 0
            continue
        # find last index from current index
        end_idx = get_end_idx_of_explosion(curr_idx, number)

        if end_idx - curr_idx + 1 >= m:  # explode
            # fill with 0
            numbers[curr_idx:end_idx + 1] = [0] * (end_idx - curr_idx + 1)
            did_explode = True

    # delete 0
    numbers = list(filter(lambda x: x > 0, numbers))

    # end if there are no more bombs left to explode
    if not did_explode:
        break

print(len(numbers))
for number in numbers:
    print(number)