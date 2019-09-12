#Write a function named minutes that takes two datetimes and, using timedelta.total_seconds() 
#to get the number of seconds, returns the number of minutes, rounded, between them. 
#The first will always be older and the second newer. You'll need to subtract the first from the second.


import datetime

first = datetime
second = datetime

def minutes(first, second):
    return round(datetime.timedelta.total_seconds(second - first) / 60)
