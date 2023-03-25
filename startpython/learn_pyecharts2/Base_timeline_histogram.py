from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType


bar1 = Bar()
bar1.add_xaxis(["china", "america", "england"])
bar1.add_yaxis("GDP", [30,20,10],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["china", "america", "england"])
bar2.add_yaxis("GDP", [50,30,20],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["china", "america", "england"])
bar3.add_yaxis("GDP", [150,50,20],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

timeline = Timeline({"theme":ThemeType.DARK})
timeline.add(bar1,"2021_GDP")
timeline.add(bar2,"2022_GDP")
timeline.add(bar3,"2023_GDP")

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

timeline.render("base timeline histogram.html")