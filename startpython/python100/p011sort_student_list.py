
students = [
    {"sno":101, "sname":"xiaozhang","sgrade":88},
{"sno":102, "sname":"lijiajia","sgrade":95},
{"sno":103, "sname":"liwushang","sgrade":89},
{"sno":104, "sname":"liwuqu1","sgrade":80},
{"sno":105, "sname":"liwuqing","sgrade":68},
]
print(f"source {students}")
student_sort = sorted(students, key = lambda x: x["sgrade"])
print(f"sort result:{student_sort}")

student_sort1 = sorted(students, key = lambda x: x["sgrade"], reverse= True)
print(f"sort result:{student_sort1}")
