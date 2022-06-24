# 두 개의 문자열 A, B가 있을 때 문자열 A를 편집하여 문자열 B로 만들고자 한다
# 삽입, 삭제, 교체를 할 수 있으며 최소 편집 거리 계산하기

a = input()
b = input()


def edit_dist(a, b):
    n = len(a)
    m = len(b)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # initialise
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # if letters are the same, insert left above number
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # if letters are different, find minimum among three
            else:
                # minimum between insert(left), delete(above), change(left above) + 1
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    return dp[n][m]

print(edit_dist(a, b))
