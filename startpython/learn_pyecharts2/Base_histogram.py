from pyecharts.charts import Bar
from pyecharts.options import *


bar = Bar()
bar.add_xaxis(["china", "america", "england"])
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))

# reverse x and y
bar.reversal_axis()


bar.render("base histogram.html")

