# -*-coding:utf-8-*-
a = [1,4,6,9,13,16,19,28,40,100,0]

input_num = int(input("entry a number:"))
# for i in range(len(a)):
#     print(a[i], i)
#     if a[i] >= input_num:
#         a.insert(i, input_num)
#         break
#
# print(a)
for i in range(len(a)):
    print(a[i], i)
    if a[i] >= input_num:
        for j in range(len(a)- i):
            # print(j)
            a[len(a)-j-1] = a[len(a)-j-2]
        a[i] = input_num
        break

print(a)






