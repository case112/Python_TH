from datetime import datetime
now = datetime.now()
time = now.strftime('%m/%d/%y')

birthday = datetime.strptime('2015-04-21 12:00', '%Y-%m-%d %H:%M')

print(time)
print(birthday)