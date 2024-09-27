import datetime

def display_current_datetime():
    format = "%Y-%m-%d %H:%M:%S"
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date.strftime(format)}")


def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.datetime.now() + timedelta(days=number_of_days)
    format = "%Y-%m-%d"
    print(f"Future date: {future_date.strftime(format)}")