# 도현이의 집 n개가 수직선 위에 있는데 집에 공유기 c개를 설치하려 한다
# c개의 공유기를 n개의 집에 적당히 설치하여 가장 인접한 두 공유기 사이의 거리를 최대로 하기

n, c = map(int, input().split())
array = [int(input()) for _ in range(n)]
array.sort()

start = 1
end = array[n - 1] - array[0]
result = 0

while start <= end:
    mid = (start + end) // 2  # gap between closest houses
    value = array[0]
    count = 1
    # try installing wifi machine
    for i in range(1, n):
        if array[i] >= value + mid:  # gap is larger than chosen gap
            value = array[i]  # install
            count += 1  # no. of installed machine
    if count >= c:  # more machine than supposed to
        start = mid + 1  # smaller gap
        result = mid
    else:
        end = mid - 1  # needs more machine, larger gap

print(result)

