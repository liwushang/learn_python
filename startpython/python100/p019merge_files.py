import os

course_teacher_dict = {}
with open("./datas/course_teacher") as fin:
    for line in fin:
        line = line[:-1]
        course, teacher = line.split(",")
        course_teacher_dict[course] = teacher

# print(course_teacher_dict)
os.system("touch ./datas/merged_list")
with open("student_three_courses_grades") as fin:
    with open("./datas/merged_list", "w") as fin1:
        for line in fin:
            line = line[:-1]
            course,sno,name,score = line.split(",")
            teacher = course_teacher_dict.get(course)
            # fin1.write(f"{course},\t{teacher},\t{sno},\t{name},\t{score}\n")
            fin1.write("%-10s\t%-10s\t%-10s\t%-10s\t%-10s\n"%(course,teacher,sno,name,score))
