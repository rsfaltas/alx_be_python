# # Display the Current Date and Time
from datetime import date,datetime, timedelta
 
def display_current_datetime():
    current_date=datetime.now()
    print("Current date and time:",current_date)

display_current_datetime()

days =int(input("Enter the number of days to add to the current date: "))
# Calculating future dates
future_time =  date.today() +timedelta(days=days)

print("Future date: ", future_time)
