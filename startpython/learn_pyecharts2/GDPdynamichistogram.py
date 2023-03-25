from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType


data_dict = {}
timeline = Timeline({"theme":ThemeType.DARK})
with open("/home/liwushang/PycharmProjects/learn_python/startpython/learn_json/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv","r",encoding="GB2312")as fin:
    data_lines = fin.readlines()
data_lines.pop(0)
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])

    try:
        data_dict[year].append([country,gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country,gdp])
sorted_year_list = sorted(data_dict.keys())

for year in sorted_year_list:
    data_dict[year].sort(key=lambda x:x[1],reverse=True)
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for i in year_data:
        x_data.append(i[0])
        y_data.append(i[1]/100000000)

    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP DATA", y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(title_opts=TitleOpts(title=f"{year}first 8 GDP"))
    timeline.add(bar,str(year))

timeline.add_schema(
    play_interval=1000,
    is_loop_play=False,
    is_auto_play=True,
    is_timeline_show=True

)




# timeline = Timeline({"theme":ThemeType.DARK})


timeline.render("GDP_dynamic_histogram.html")

