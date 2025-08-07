#1. Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

current_datetime = datetime.now()
day = current_datetime.day
month = current_datetime.month
year = current_datetime.year
hour = current_datetime.hour
minute = current_datetime.minute
timestamp = current_datetime.timestamp()
print(f"Day: {day}, Month: {month}, Year: {year}, Hour: {hour}, Minute: {minute}, Timestamp: {timestamp}")


#2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_date = current_datetime.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Formatted Date: {formatted_date}")

#3. Today is 5 December, 2019. Change this time string to time

time_string = "5 December, 2019"
time = datetime.strptime(time_string, "%d %B, %Y")
print(f"Time Object: {time}")

#4. Calculate the time difference between now and new year.
new_year = datetime(year + 1, 1, 1)
print(f"New Year: {new_year}")
time_difference = new_year - current_datetime
print(f"Time until New Year: {time_difference}")

#5. Calculate the time difference between 1 January 1970 and now.
epoch_time = datetime(1970, 1, 1)
time_difference_epoch = current_datetime - epoch_time
print(f"Time since Epoch: {time_difference_epoch}")

#6. Think, what can you use the datetime module for?
# - Scheduling tasks
# - Logging events with timestamps
# - Calculating time differences
# - Formatting dates for display
# - Handling time zones
# - Parsing and validating date strings
# - Creating reminders or alarms
# - Working with durations and intervals
# - Converting between different date formats
# - Managing deadlines and due dates
