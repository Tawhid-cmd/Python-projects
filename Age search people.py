people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 40},
    {'name': 'David', 'age': 22},
    {'name': 'Ezaz', 'age': 25}
]

while True:
    age = int(input("Enter your age (or a negative number to stop): "))

    if age < 0:
        break

    # Search for people with the given age
    found_people = []
    for person in people:
        if person['age'] == age:
            found_people.append(person['name'])

    # Print the people's names if found
    if found_people:
        print("The following people have the age", age, ":", found_people)
    else:
        print("Sorry, no person found with age", age)

