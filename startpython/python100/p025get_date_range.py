import datetime

begin_date = "2021-04-28"
end_date = "2021-05-03"

begin_date_obj = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
end_date_obj = datetime.datetime.strptime(end_date, "%Y-%m-%d")
gap_day = end_date_obj - begin_date_obj
print(gap_day.days)

for day in range(gap_day.days+1):
    print(day)
    time_gap = datetime.timedelta(day)
    print((begin_date_obj + time_gap).strftime("%Y-%m-%d"))
