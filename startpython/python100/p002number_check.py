def Get_jiecheng(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result
print(Get_jiecheng(4))
print(Get_jiecheng(100))
print(Get_jiecheng(3))