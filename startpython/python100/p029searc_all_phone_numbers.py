import re
content = """
fdvjndfiov15529571111degerg,bdfdfbdv,15529573711.egf15529571981edgf15529571111
15529571111,155295711,155271111.155295711
dsefg15529571151 15529572211
"""
content1 = "15529571111"
# start with 1, number 11,the second number:3~9
pattern = r"1[3-9]\d{9}"
alllist = re.findall(pattern, content)
print(alllist)
for i in alllist:
    print(i)
