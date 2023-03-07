import datetime

unix_time = 1620747647
datetime_obj = datetime.datetime.fromtimestamp(unix_time)
print(datetime_obj.strftime("%Y-%m-%d"))

