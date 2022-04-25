# 부품 찾기

# shop inventory
n = int(input())
shop_part = list(map(int, input().split()))

# customer's order
m = int(input())
cust_part = list(map(int, input().split()))

# search cust_part in shop_part
# using in
for part in set(cust_part):
    if part in shop_part:
        print("yes", end=" ")
    else:
        print("no", end=" ")


# using binary search
def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if target == array[mid]:
        return True
    elif target < array[mid]:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

print()
shop_part = sorted(shop_part)
for part in cust_part:
    answer = binary_search(shop_part, part, 0, n - 1)
    if answer is True:
        print('yes', end=" ")
    else:
        print('no', end=" ")
