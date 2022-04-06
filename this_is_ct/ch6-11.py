# 성적이 낮은 순서로 학생 출력하기

n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append((name, int(score)))


st_sorted = sorted(students, key=lambda student: student[1])
for st in st_sorted:
    print(st[0], end=" ")
