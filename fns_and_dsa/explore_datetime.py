import datetime

def display_current_datetime():
    # Obtain the current date and time
    current_date = datetime.datetime.now()
    # Format and print the current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    # Prompt the user to enter a number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Calculate the future date by adding the specified number of days
    future_date = datetime.datetime.now() + datetime.timedelta(days=days_to_add)
    # Print the future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
