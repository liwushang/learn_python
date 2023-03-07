# -*-coding:utf-8-*-

a = [9,6,5,4,1]
for i in (range((len(a)-1)//2)):
    print(a[i], a[len(a)-1-i])
    tmp = a[i]
    a[i] = a[len(a)-1-i]
    a[len(a)-1-i] = tmp

print(a)