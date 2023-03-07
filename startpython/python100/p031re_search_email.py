import re


content = """
    liwushang12423@qq.com
    tangsadaf#abc.com
    zuopython666@163.cnzuozhe:jaidao
    zhizaipython_ant-666@sina.netzhizaicishangzhong
    liwuqu1vsd23@qq.com
"""
pattern = re.compile(r"""
    [a-zA-Z0-9_-]+
    @
    [a-zA-A0-9]+
    \.
    [a-zA-Z]{2,4}
""", re.VERBOSE)

result = pattern.findall(content)
for item in result:
    print(item)
