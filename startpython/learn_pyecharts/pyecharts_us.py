import json
import os
import sys
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts,LabelOpts


with open("/startpython/learn_json/可视化案例数据/折线图数据/美国.txt", "r") as fin:
    reads = fin.read()
    reads = reads.replace("jsonp_1629344292311_69436(", "")
    reads = reads[:-2]
    # print(reads)
us_dict = json.loads(reads)
us_trend_data = us_dict["data"][0]["trend"]
us_x_data = us_trend_data["updateDate"]
us_x_data = us_x_data[:314]
us_y_data = us_trend_data["list"][0]["data"][:314]
line = Line()
line.add_xaxis(us_x_data)
line.add_yaxis("us_death_number", us_y_data, label_opts=LabelOpts(is_show=False))


with open("/startpython/learn_json/可视化案例数据/折线图数据/印度.txt", "r") as fin:
    reads = fin.read()
    reads = reads.replace("jsonp_1629350745930_63180(", "")
    reads = reads[:-2]
    # print(reads)
india_dict = json.loads(reads)
india_trend_data = india_dict["data"][0]["trend"]
india_x_data = india_trend_data["updateDate"]
india_x_data = india_x_data[:314]
india_y_data = india_trend_data["list"][0]["data"][:314]
line.add_yaxis("india_death_number", india_y_data, label_opts=LabelOpts(is_show=False))

with open("/startpython/learn_json/可视化案例数据/折线图数据/日本.txt", "r") as fin:
    reads = fin.read()
    reads = reads.replace("jsonp_1629350871167_29498(", "")
    reads = reads[:-2]
    # print(reads)
japan_dict = json.loads(reads)
japan_trend_data = japan_dict["data"][0]["trend"]
japan_x_data = japan_trend_data["updateDate"]
japan_x_data = japan_x_data[:314]
japan_y_data = japan_trend_data["list"][0]["data"][:314]
line.add_yaxis("japan_death_number", japan_y_data, label_opts=LabelOpts(is_show=False))



line.set_global_opts(
    title_opts=TitleOpts(title="2020 year Death", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    # toolbox_opts=ToolboxOpts(is_show=True),
    # visualmap_opts=VisualMapOpts(is_show=True)
)



line.render()
