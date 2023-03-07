def read_file():
    result = []
    with open ("./student_grade_input.txt") as fin:
        for line in fin:
            line = line[:-1]
            result.append(line.split(","))
    return result

def sort_grades(datas):
    return sorted(datas, key = lambda x: float(x[2]), reverse=True)

def write_file(datas):
    with open("./student_grade_output.txt", "w") as fout:
        for data in datas:
            fout.write(",".join(data)+"\n")


# read file
datas = read_file()
print(datas)
# sort data

newdatas = sort_grades(datas)
print(newdatas)
# write file
write_file(newdatas)