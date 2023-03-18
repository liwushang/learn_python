import os
import sys
import json

with open("/home/liwushang/PycharmProjects/learn_python/startpython/learn_json/可视化案例数据/折线图数据/美国.txt","r") as fin:
    reads = fin.read()
    reads = reads.replace("jsonp_1629344292311_69436(", "")
    reads = reads[:-2]
    # print(reads)
us_dict = json.loads(reads)
# print(us_dict, type(us_dict))
trend_data = us_dict["data"][0]["trend"]
# print(trend_data)
x_data = trend_data["updateDate"]
x_data = x_data[:314]
print(x_data)
y_data = trend_data["list"][0]["data"][:314]
print(y_data)

