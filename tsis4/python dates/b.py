#Write a Python program to print yesterday, today, tomorrow.
import datetime

# Get today's date
today = datetime.date.today()

# Get yesterday's date
yesterday = today - datetime.timedelta(days=1)

# Get tomorrow's date
tomorrow = today + datetime.timedelta(days=1)

# Print the dates
print("Yesterday's date: ", yesterday)
print("Today's date: ", today)
print("Tomorrow's date: ", tomorrow)