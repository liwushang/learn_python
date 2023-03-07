import os

data_dir = "./datas/many_texts"
file_list = []
for file in os.listdir(data_dir):
    file_path = f"{data_dir}/{file}"
    if os.path.isfile(file_path) and file.endswith(".txt"):
        print(file_path)
        with open(file_path) as fin:
            file_list.append(fin.read())

final_content = "\n".join(file_list)
print(file_list)
print(final_content)

with open("./datas/many_texts.txt", "w") as fin:
    fin.write(final_content)

