#Write a Python program to drop microseconds from datetime.
import datetime

# Get the current datetime with microseconds

now = datetime.datetime.now()

# Drop the microseconds
now_without_microseconds = now.replace(microsecond=0)

# Print the datetime without microseconds
print("Datetime with microseconds:", now)
print("Datetime without microseconds:", now_without_microseconds)