student_number = int(input())

student_record = {}

for _ in range(student_number):
    student_grade = input().split()
    student = student_grade[0]
    grade = float(student_grade[1])

    if student not in student_record:
        student_record[student] = []
    student_record[student].append(grade)

for name, grade in student_record.items():
    average = sum(grade) / len(grade)
    grades_as_str = [f"{el :.2f}" for el in grade]
    print(f"{name} -> {' '.join(grades_as_str)} (avg: {average :.2f})")