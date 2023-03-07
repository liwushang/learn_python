# -*-coding:utf-8-*-
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

a=[]
b=[]
c = []
for line in X:
    for item in line:
        a.append(item)
for line in Y:
    for item in line:
        b.append(item)
print(a, b)

for i in range(len(a)):
    tmp = a[i]+b[i]
    c.append(tmp)
print(c)

result = [[0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j]+Y[i][j]
print(result)

