
from datetime import date,datetime, timedelta
 
def display_current_datetime():
    current_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:",current_date)

display_current_datetime()

def calculate_future_date():
    days =int(input("Enter the number of days to add to the current date: "))
    # Calculating future dates
    future_time =  date.today() +timedelta(days=days)
    future_time= future_time.strftime("%Y-%m-%d")
    print("Future date: ", future_time)

calculate_future_date()
