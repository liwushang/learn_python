import datetime
date_sale = {}
datelist = []
is_first_line = True
with open("./datas/date_sale_data.txt") as fin:
    for line in fin:
        if is_first_line:
            is_first_line = False
            continue
        line = line[:-1]
        date, sale_number = line.split("\t")
        # print(f"date{date}, sale_number{sale_number}")
        date_sale[date] = float(sale_number)

def get_diff_days(date, datecount):
    for i in date_sale.keys():
        datelist.append(i)
    for j in range(len(datelist)):
        if date == datelist[j]:
            if j -datecount >=0:
                return datelist[j-datecount]
            else:
                return date
def new_get_diff_days(date, days):
    curr_date = datetime.datetime.strptime(date, "%Y/%m/%d")
    timedelta = datetime.timedelta(days=-days)
    return (curr_date + timedelta).strftime("%Y/%m/%d")

date7 = get_diff_days('2021/5/8', 7)
newdate7 = new_get_diff_days('2021/5/8', 7)
print(date7)
print(newdate7)
for date, sale_number in date_sale.items():
    date7 = get_diff_days(date, 7)
    sale_number7 = date_sale.get(date7, 0)
    if sale_number7 == 0:
        print(date, sale_number, 0)
    else:
        weekdiff = (sale_number-sale_number7)/sale_number7
        print(date,sale_number,date7,sale_number7,weekdiff)