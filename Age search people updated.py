from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age_months = today.month + 12 - birthdate.month - (today.day < birthdate.day)
    else:
        age_months = today.month - birthdate.month
        
    age_days = (today - birthdate).days % 30
    
    return age_years, age_months, age_days

# Define a dictionary of persons and their birthdates
persons = {
    "Alice": date(1985, 8, 12),
    "Bob": date(1990, 5, 15),
    "Charlie": date(1977, 11, 30)
}

# Prompt the user to enter a person's name
name = input("Enter a person's name: ")

# Look up the person's birthdate
if name in persons:
    birthdate = persons[name]
    age_years, age_months, age_days = calculate_age(birthdate)
    print(name + "'s age is:", age_years, "years,", age_months, "months, and", age_days, "days.")
else:
    print("Sorry, I don't know that person.")

