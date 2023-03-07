import datetime

birthday = "2022-12-13"
m_year, m_mouth, m_day = birthday.split("-")
print(m_year, m_mouth,m_day)
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
print(birthday_date, type(birthday_date))

curr_datetime = datetime.datetime.now()

minus_datetime = birthday_date - curr_datetime
print(minus_datetime, type(minus_datetime))
