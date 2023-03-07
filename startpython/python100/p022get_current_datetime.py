
import datetime

curr_datetime = datetime.datetime.now()
print(curr_datetime)

print(curr_datetime, type(curr_datetime))
str_time = curr_datetime.strftime( "%Y-%m-%d %H:%M:%S")
print(str_time, type(str_time))

print(curr_datetime.year)
print(curr_datetime.month)
print(curr_datetime.day)
print(curr_datetime.hour)
