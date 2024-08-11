'''
Exercise 2 : Cinemax #2
Instructions
A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.

Given the following object:

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


How much does each family member have to pay ?

Print out the family’s total cost for the movies.
Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

'''

family = {}

while True:
    
    name = input('Write the name of the person. If you want to quit, type "quit"')
    if name == 'quit':
        break
    
    age = input('Write the age of the person. If you want to quit, type "quit"')
    if age == 'quit':
        break

    family[name] = int(age)

price = 0
for name, age in family.items():
    if 3 < age <= 12:
        price += 10
    elif age > 12:
        price += 15

print(f'Total coast for the movie {price}')