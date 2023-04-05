from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Prompt the user to enter their birthdate
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = date.fromisoformat(birthdate_str)

# Calculate the user's age
age = calculate_age(birthdate)

# Print the user's age
print("Your age is:", age)


