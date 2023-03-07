# -*-coding:utf-8-*-

def compare_number(a,b):
    result = ""
    if a > b:
        result = f"number {a} is lager than {b}"
    if a < b:
        result = f"number {a} is less than {b}"
    if a == b:
        result = f"number {a} is equal to {b}"
    return result
if __name__ == '__main__':
    x = 20
    y = 20
    result = compare_number(x,y)
    print(result)
