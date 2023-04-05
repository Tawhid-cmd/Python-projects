from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

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
    age = calculate_age(birthdate)
    print(name + "'s age is:", age)
else:
    print("Sorry, I don't know that person.")



