# -*-coding:utf-8-*-
print("while input number is more than 50 ,the programme will end")
flag=1
result = 0
while flag:
    input_number = int(input("input your number:"))
    if input_number <= 50:
        result = input_number * input_number
        print(result)
    else:
        print("you input number is out range")
        flag=0

print("programme is over")

