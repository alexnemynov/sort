from datetime import date
from dateutil.relativedelta import relativedelta, TH

def free_days(year):
    return map(lambda x: x.strftime("%d.%m.%Y"), [date(year, m, 1) + relativedelta(weekday=TH(3)) for m in range(1, 13)])


year = int(input())
print(*free_days(year), sep='\n')