#Write a Python program to calculate two date difference in seconds.
import datetime

# Get the first date from the user
date1_str = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")

# Get the second date from the user
date2_str = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")
date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

# Calculate the difference between the two dates in seconds
difference = abs((date2 - date1).total_seconds())

# Print the result
print("The difference between the two dates is", difference, "seconds.")
#2022-01-01 12:45:45
