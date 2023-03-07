# -*-coding:utf-8-*-
num = 2
def autofunc():
    num =1
    print('internal block bum = %d' % num)
    num +=1

for i in range(3):
    print("the num = %d" % num)
    num+=1
    autofunc()