# key:course, value:grade list
course_grades = {}

with open("student_three_courses_grades") as fin:
    for line in fin:
        line = line[:-1]
        course, stunumber, name, score = line.split(",")
        if course not in course_grades:
            course_grades[course] = []
        course_grades[course].append(int(score))
        print("{},{},{},{}".format(course, stunumber, name, score))

print(course_grades)

for course, grades in course_grades.items():
    print(course, max(grades), min(grades),sum(grades)/len(grades))