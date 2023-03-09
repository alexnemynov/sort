from datetime import datetime
import pytz  # pip install pytz

dt = datetime(2022, 6, 4)
nyc = pytz.timezone("America/New_York")

localized = nyc.localize(dt)
print(f"Datetime: {localized}, Timezone: {localized.tzname()}, TZ Info: {localized.tzinfo}")

# По-новому:
from zoneinfo import ZoneInfo, available_timezones  # pip install tzdata

nyc = ZoneInfo("America/New_York")
localized = datetime(2022, 6, 4, tzinfo=nyc)
print(f"Datetime: {localized}, Timezone: {localized.tzname()}, TZ Info: {localized.tzinfo}")
# Datetime: 2022-06-04 00:00:00-04:00, Timezone: EDT, TZ Info: America/New_York
print(localized.astimezone(ZoneInfo("Europe/Moscow")))
# 2022-06-04 07:00:00+03:00
for key in available_timezones():
    print(key)