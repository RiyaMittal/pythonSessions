# date time is of importance in python

import time, calendar

print(time.time())  # this will give number of ticks from epoch( i.e, 1 Jan 1970)
# what is a tick?
# Ticks are floating point numbers measured in units of seconds for time interval.

print(time.ctime())  # human readable format
#
time.sleep(5)
print("sleep ended now")
#
# #########################################################################
#
print(calendar.month(2023, 1))
