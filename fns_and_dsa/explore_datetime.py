from datetime import datetime, timedelta
now = datetime.now()
print(f"Current date and time: {now}")
number_of_days = int(input("Enter the number of days to add to the current date: "))


def calculate_future_date(number_of_days):
    return now + timedelta(days=number_of_days)


print(f"Future date: {calculate_future_date(number_of_days)}")
