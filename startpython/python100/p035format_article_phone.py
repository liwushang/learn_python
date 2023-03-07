# -*-coding:utf-8-*-
content = "bairiyi2021/05/26shangjing,huangheru2021.05.27hailiu." \
          "yuqing05-28-2020qianlimu, gengshang5/29/2020yicenglou"

import re

content = re.sub(r"(\d{4})/(\d{2})/(\d{2})", r"\1-\2-\3", content)
content = re.sub(r"(\d{4})\.(\d{2})\.(\d{2})", r"\1-\2-\3", content)
content = re.sub(r"(\d{2})-(\d{2})-(\d{4})", r"\3-\1-\2", content)
content = re.sub(r"(\d{1,2})/(\d{2})/(\d{4})", r"\3-\1-\2", content)
print(content)
