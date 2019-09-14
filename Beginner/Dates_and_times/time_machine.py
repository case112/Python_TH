import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

# Remember, you can't set "years" on a timedelta!
# Consider a year to be 365 days.

## Example
# time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)


def time_machine(num, time):
    if time == 'years':
        time = 'days'
        num *= 365
    return starter + datetime.timedelta(**{time: num})
