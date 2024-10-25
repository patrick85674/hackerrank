
# HackerRank challenge: nested list
# Sort students by second lowest grade

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2],
            ['Akriti', 41], ['Harsh', 39]]

student_count = len(students)
first_student = students[0]
lowest_grade = students[0][1]
second_lowest_grade = 101
grade_list = {lowest_grade: [first_student]}

index = 1

while index < student_count:
    next_student = students[index]
    next_student_grade = students[index][1]
    if next_student_grade < lowest_grade:
        second_lowest_grade = lowest_grade
        lowest_grade = next_student_grade
    elif next_student_grade < second_lowest_grade:
        second_lowest_grade = next_student_grade
    grade_student_list = grade_list.get(next_student_grade, None)
    if grade_student_list is None:
        grade_list.update({next_student_grade: [next_student]})
    else:
        grade_student_list.append(next_student)

    index += 1

grade_list[second_lowest_grade].sort()
print("Students with the second lowest grade:")
for student in grade_list[second_lowest_grade]:
    print(student[0])
