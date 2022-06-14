# n명의 이름과 국영수 점수가 주어질 때
# 국어 점수 감소 / 국어 점수 같으면 영어 점수 증가 순서 /
# 국어 영어 점수 같으면 수학 점수가 감소하는 순서
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 정렬하기

n = 12
students = [["Junkyu", 50, 60, 100], ["Sangkeun", 80, 60, 50], ["Sunyoung", 80, 70, 100], ["Soong", 50, 60, 90],
["Haebin", 50, 60, 100], ["Kangsoo", 60, 80, 100], ["Donghyuk", 80, 60, 100], ["Sei", 70, 70, 70],
["Wonseob", 70, 70, 90], ["Sanghyun", 70, 70, 80], ["nsj", 80, 80, 80], ["Taewhan", 50, 60, 90]]

#                            descending, ascending, descending, ascending
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])
