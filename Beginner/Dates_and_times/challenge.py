#Write a function named minutes that takes two datetimes and, using timedelta.total_seconds() 
#to get the number of seconds, returns the number of minutes, rounded, between them. 
#The first will always be older and the second newer. You'll need to subtract the first from the second.


import datetime

first = datetime
second = datetime

def minutes(first, second):
    return round(datetime.timedelta.total_seconds(second - first) / 60)
  
  
## Examples
# to_string(datetime_object) => "24 September 2012"
# from_string("09/24/12 18:30", "%m/%d/%y %H:%M") => datetime
import datetime
def to_string(job):
    return job.strftime('%d %B %Y')

def from_string(date, frmat):
    return datetime.strptime(date, frmat)
    
    
    

