#continue는 아래이 문장이 실행되지 않고 바로 위 조건문으로 넘어가라는 뜻

absent = [2, 5]
for student in range(1, 11):
    if student in absent:
        continue
    print("{0}, 책을 읽어봐!".format(student))


absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 끝!. {0}는 교무실로 따라와!".format(student))
        break
    print("{0}, 책 읽어봐!".format(student))

# 출석번호가 1,2,3,4 앞에 100을 붙이기로 함

students = [1,2,3,4,5]
print(student)
students = [i+100 for i in students]
print(students)

# 학생 이름을 대문자로 변환

students = ["Iron man", "Thor", "I am Groot"]
students = [i.upper() for i in students]
print(students)
