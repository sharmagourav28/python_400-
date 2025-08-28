from datetime import datetime


def diff_date(date1, date2):
    return abs((date2 - date1).days) + 1


date1 = datetime(2020, 10, 21)
date2 = datetime(2021, 10, 22)
print(diff_date(date1, date2))
