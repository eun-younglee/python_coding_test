#  시각

n = int(input())
cnt = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)  # make into string
            if '3' in time:  # check if there's three
                cnt += 1

print(cnt)