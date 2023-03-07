# -*-coding:utf-8-*-

import jieba.posseg as posseg

content = "黎明喜欢李嘉嘉，他俩早恋了"

for word, flag in posseg.cut(content):
    if flag == "nr":
        print(word, flag)
print(content)

del content

print(content)
