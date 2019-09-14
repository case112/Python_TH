import datetime
import pytz

pacific = pytz.timezone('US/Pacific')
eastern = pytz.timezone('US/Eastern')
fmt = '%Y/%m/%d %H:%M:%S, %Z%z'
utc = pytz.utc

start = pacific.localize(datetime.datetime(2019, 5, 21, 10))
print(start.strftime(fmt))

start_eastern = start.astimezone(eastern)

print(start_eastern)
