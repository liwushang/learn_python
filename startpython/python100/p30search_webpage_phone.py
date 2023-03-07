import re


pattern = r"1[3-9]\d{9}"
file_content = ""
with open("datas/phone_number.txt") as fin:
    file_content = fin.read()
print(file_content)
all_number = re.findall(pattern, file_content)
for number in all_number:
    print(number)
