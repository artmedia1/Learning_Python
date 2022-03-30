#https://docs.python.org/3/library/time.html

import time as t
import calendar
print(t.localtime())

time_now = t.localtime()

print("Transaction completed at:", str(time_now.tm_hour) + "h " + str(time_now.tm_min) + "m on " + calendar.month_name[time_now.tm_mon] + " " + str(time_now.tm_mday) + " " + str(time_now.tm_year))

print(t.time())
# Shows the number of seconds that have passed since the epoch, python uses the unix epoch

# The Unix epoch (or Unix time or POSIX time or Unix timestamp) is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), 
# not counting leap seconds (in ISO 8601: 1970-01-01T00:00:00Z). Literally speaking the epoch is Unix time 0 (midnight 1/1/1970), but 'epoch' is often 
# used as a synonym for Unix time. Some systems store epoch dates as a signed 32-bit integer, which might cause problems on January 19, 2038 (known as the Year 2038 problem or Y2038). 
# The converter on this page converts timestamps in seconds (10-digit), milliseconds (13-digit) and microseconds (16-digit) to readable dates.

#say we want the delivery time of something exactly 7 days from now

time_now = t.time()
week_From_Now = time_now + (86400 * 7) # number of seconds in a day * 7
delivery_time = t.localtime(week_From_Now)
 

print("The delivery will be completed at:", str(delivery_time.tm_hour) + "h " + str(delivery_time.tm_min) + "m on " + calendar.month_name[delivery_time.tm_mon] + " " + str(delivery_time.tm_mday) + " " + str(delivery_time.tm_year))
                                   
t.sleep(5) #Delays input for 5 seconds