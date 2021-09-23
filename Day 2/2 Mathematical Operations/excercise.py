current_age = int(input("Enter your age :"))
final_year = 90
year_left = final_year - current_age
days_remaining = year_left*365
weeks_remaining = year_left*52
months_remaining = year_left*12
message = f"You've {days_remaining} days or {weeks_remaining} weeks or {months_remaining} months left"
print(message)
