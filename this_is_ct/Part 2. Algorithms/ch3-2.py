# 큰 수의 법칙

n, m, k = map(int, input().split())
num = list(map(int, input().split()))
max_num = max(num)  # 가장 큰 수
num.remove(max_num)
sec_num = max(num)  # 두 번째로 큰 수
total = 0

# 가장 큰 수가 더해지는 횟수
count = m // (k + 1) * k
count += m % (k + 1)

total += count * max_num
total += (m - count) * sec_num  # 두번째로 큰 수 더하기

print(total)
