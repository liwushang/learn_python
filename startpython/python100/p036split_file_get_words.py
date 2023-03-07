# -*-coding:utf-8-*-
import re
import pandas as pd
with open("./voa.txt") as fin:
    content = fin.read()

words = re.split(r"[\s.()-?]+", content)
print(words)

a = pd.Series(words).value_counts()
print(a)

