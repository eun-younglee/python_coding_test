# 점수가 주어졌을 때 점수를 자릿수 기준으로 반으로 나누기
# 왼쪽 부분의 각 자릿수 합과 오른쪽 부분의 각 자릿수 합이 동일하면 LUCKY, 아니면 READY

def split(num):  # turn string into list of int
    return [int(n) for n in num]


score = input()
half = len(score) // 2

fore = split(score[:half])
rear = split(score[half:])
if sum(fore) == sum(rear):
    print("LUCKY")
else:
    print("READY")