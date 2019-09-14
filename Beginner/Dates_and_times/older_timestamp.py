import datetime
import time

# If you need help, look up datetime.datetime.fromtimestamp()
# Also, remember that you *will not* know how many timestamps
# are coming in.

def timestamp_oldest(*args):
    # this uses args, so we have to convert it to a list
    ts_list = list(args)
    # sort the list
    ts_list.sort()
    # return the first element in the list
    ts_list[0]
    
    # make the timestamp a date_object
    older_dt = datetime.datetime.fromtimestamp( ts_list[0])
    return older_dt
    print("The older datetime object = {}".format(older_dt))

