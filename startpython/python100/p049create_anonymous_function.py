# -*-coding:utf-8-*-

maximum = lambda x, y: (x>y)*x+(y>x)*y
minmum = lambda x ,y : (x>y)*y+(y>x)*x
print(maximum(12, 8))
print(minmum(12, 8))