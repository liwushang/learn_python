def read_file():
    result = []
    scores = []
    with open ("student_grade_input.txt") as fin:
        for line in fin:
            line = line[:-1]
            fields = line.split(",")
            result.append(line.split(","))
            scores.append(int(fields[-1]))
        # convenient method:max(scores), min(scores), avg  = sum(scores)/len(scores)
    return result, scores

def computer_max_min_avg(datas, scores):
    result = []
    reslut = sorted(datas, key = lambda x:int(x[2]))
    minlist = reslut[0]
    min = minlist[2]
    maxlist = reslut[-1]
    max = maxlist[2]
    avg = 0
    i = 0
    total = 0
    for item in scores:
        i+= 1
        total += int(item)
    avg = total/i

    return (min, max,avg)
file_list, score_list = read_file()
# print(file_list)
# print("score:", score_list)
min_score, max_score, avg_score = computer_max_min_avg(file_list, score_list)
# print(f"max:{max_score}, min:{min_score}, avg :{avg_score}")
