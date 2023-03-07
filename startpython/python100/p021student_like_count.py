
ball_like_dict ={}
with open("./datas/student_like.txt")as fin:
    for line in fin:
        line = line[:-1]
        name, words = line.split(" ,")
        balls = words.split(",")
        print(balls)
        for ball in balls:
            if ball not in ball_like_dict:
                ball_like_dict[ball] = 0
            ball_like_dict[ball] += 1



print(ball_like_dict)

