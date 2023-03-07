# -*-coding:utf-8-*-
import mypackage


# print(mypackage)
print(mypackage.B)

print(dir(mypackage))
import mypackage.mymodule
print(dir(mypackage))

import mypackage.mymodule as m
print(dir(mypackage))