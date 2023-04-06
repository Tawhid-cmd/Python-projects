from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        months = 12 - birthdate.month + today.month - 1
    else:
        months = today.month - birthdate.month
    days = (today - birthdate.replace(year=today.year)).days
    return age, months, days

# Prompt the user to enter their birthdate
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = date.fromisoformat(birthdate_str)

# Calculate the user's age
age, months, days = calculate_age(birthdate)

# Print the user's age
print("Your age is:", age, "years,", months, "months, and", days, "days.")


