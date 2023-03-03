#Write a Python program to subtract five days from current date.
import datetime
current_date=datetime.date.today()
five_days=datetime.timedelta(days=5)
new_date=current_date-five_days

print("Current date : " , current_date)
print("Five days ago was : " , new_date)