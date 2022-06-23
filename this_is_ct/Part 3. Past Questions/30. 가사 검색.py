# 가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는지 알아보기
# 각 키워드 별로 매치된 단어가 몇 개인지 배열에 담아 반환하기
from bisect import bisect_left, bisect_right

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

array = [[] for _ in range(10001)]  # 10001 because length of words in queries is maximum 10000
reversed_array = [[] for _ in range(10001)]


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)  # words smaller than queries + z
    left_index = bisect_left(a, left_value)  # words bigger than queries + a
    return right_index - left_index


def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)  # append word to index of word length
        reversed_array[len(word)].append(word[::-1])  # append reversed word

    for i in range(10001):  # order alphabetically
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[0] != '?':  # ? in the back
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:  # ? in the front
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)
    return answer


print(solution(words, queries))
