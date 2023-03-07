import re
def date_is_right(date):
    return re.match(r"\d{4}-\d{2}-\d{2}", date) is not None

date1 = "2021-05-20"
date2 = "202-05-20"
date3 = "2021/05-20"
date4 = "20210520"
print(date_is_right(date1))

