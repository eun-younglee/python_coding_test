# 떡볶이 떡 만들기

n, m = map(int, input().split())
tteok = list(map(int, input().split()))

start = 0
end = max(tteok)  # max length among tteoks
cut_length = 0  # will cut at this length

while start <= end:
    total = 0  # cut off tteoks
    mid = (start + end) // 2
    for t in tteok:
        if t > mid:
            total += t - mid
    if total < m:  # have to cut more
        end = mid - 1  # check forepart
    else:  # have to cut less
        result = mid  # answer candidate
        start = mid + 1  # check rear part

print(result)
