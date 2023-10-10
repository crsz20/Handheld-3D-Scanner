from datetime import datetime
from dateutil import tz

date_and_time = datetime.now()
date = date_and_time.date()
timestamp = datetime.utcfromtimestamp(date_and_time.timestamp())

print("Date: ", date)
date_str = date.isoformat() + "hi"
print("Date: ", date_str)
print(date.isoformat())

from_local_zone = tz.tzutc()
to_local_zone = tz.tzlocal()
utc = date_and_time.replace(tzinfo=from_local_zone)
central = utc.astimezone(to_local_zone)

timestamp_hour = central.hour
timestamp_minute = central.minute
timestamp_second = central.second

print(timestamp)
# timestamp_str = timestamp.utcnow() + "hi"
print("Central: ", central)
print("====MY TIMESTAMP===")
print(str(timestamp_hour) + " " + str(timestamp_minute) + " " + str(timestamp_second))


# create a datetime object representing March 1, 2023 at 9:30 AM
start_datetime = datetime(2023, 3, 1, 9, 30)
start_datetime2 = datetime(2023, 3, 1, 9, 29)

# get the year, month, day, hour, and minute
year = start_datetime.year
month = start_datetime.month
day = start_datetime.day
hour = start_datetime.hour
minute = start_datetime.minute

print(start_datetime > start_datetime2)