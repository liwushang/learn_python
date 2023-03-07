# -*-coding:utf-8-*-
content = """
fdvjndfiov15529571111degerg,bdfdfbdv,15529573711.egf15529571981edgf15529571111
15529571111,155295711,155271111.155295711
dsefg15529571151 15529572211
"""

import re

pattern = r"(1[3-9]\d{1})\d{4}(\d{4})"
a = re.sub(pattern, r"\1***\2", content)
print(a)
