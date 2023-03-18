import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

map = Map()
data = [
    ("北京", 99),
    ("上海", 166),
    ("湖南", 567),
    ("陕西", 657),
    ("天津", 547)
]
map.add("test map", data, "china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"laobel":"1-9","color":"#CCFFFF"},
{"min":10,"max":99,"laobel":"10-99","color":"#FF6666"},
{"min":100,"max":999,"laobel":"100-9999","color":"#990033"}
        ]
        # pieces=
    )
)
map.render()

