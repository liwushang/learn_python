from pyecharts.charts import Map
from pyecharts.options import *

import json
with open("/home/liwushang/PycharmProjects/learn_python/startpython/learn_pyecharts/可视化案例数据/地图数据/疫情.txt","r")as fin:
    reads = fin.read()

data_dict = json.loads(reads)
province_data_list = data_dict["areaTree"][0]["children"]
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))

map = Map()
map.add("human number", data_list, "china")
map.set_global_opts(
    title_opts=TitleOpts(title = "all province map"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"label":"1-99","color":"#CCFFFF"},
{"min":100,"max":999,"label":"100-999","color":"#FFFF99"},
{"min":1000,"max":9999,"label":"1000-9999","color":"#FF9966"},
{"min":10000,"max":99999,"label":"10000-99999","color":"#FF6666"},
{"min":100000,"max":999999,"label":"100000-999999","color":"#CC3333"},
{"min":1000000,"max":9999999,"label":"1000000-9999999","color":"#990033"},
        ]
    )
)

map.render()
