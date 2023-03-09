from datetime import timezone, timedelta, datetime
import pytz

td = timedelta(hours=3)
print(timezone(td))

dt = datetime.now()
print()

print(dt)
print(dt.tzinfo)
print(dt.tzname())
print(dt.dst())

timezone = pytz.timezone('Europe/Moscow')
mydt = timezone.localize(dt)
print()

print(mydt)
print(mydt.tzinfo)
print(mydt.tzname())
print(mydt.dst())


