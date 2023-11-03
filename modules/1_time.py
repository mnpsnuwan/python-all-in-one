# epoch = A date and time from which a computer measures system time.
# When your computer thinks time began (reference point)

import time

print(time.ctime())
print(time.ctime(0))  # Convert a time expressed in second since epoch to a readable string
print(time.ctime(10000))  # Passing ms

print(time.time())  # Return current seconds since epoch

print(time.ctime(time.time()))  # Current date and time, same as 'print(time.ctime())'

time_object = time.localtime()
time_object_utc = time.gmtime()

print(time_object)

local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)  # Convert above time_object to readable format
print(local_time)


time_string = "20 April, 2023"
time_object_strp = time.strptime(time_string, "%d %B, %Y")

print(time_object_strp)

# time_tuple (year, month, day, hours, minutes, secs, #day of the week, #day of the year, day-light saving time)
time_tuple = (2023, 11, 3, 10, 15, 7, 0, 0, 0)
print(time.asctime(time_tuple))
print(time.mktime(time_tuple))  # time_tuple in seconds
