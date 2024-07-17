import datetime as dt
import time as t

def time_stamp():
    return t.time()
# Using:
# print(f"Seconds since January 1, 1970: {time_stamp:,.4f} or {time_stamp:.2e} in scientific notation")


def current_time():
    return dt.datetime.now()

# printing current date in "Mon day year" format
# print(current_time.strftime("%b %d %Y"))