# -*-coding:utf-8-*-

def exchange_value(a,b):
    tmp=0
    tmp =a
    a= b
    b= tmp
    return a,b
if __name__ == '__main__':
    x = 10
    y= 20
    x,y = exchange_value(x,y)
    print(x,y)
