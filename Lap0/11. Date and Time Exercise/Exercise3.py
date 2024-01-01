from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25)
print("Given date")
print(given_date)

days_to_subtract = 7
result = given_date - timedelta(days=days_to_subtract)
print("New Date")
print(result)
