'''
Exercise 7 : Faker Module
Instructions
Install the faker module, and take a look at the documentation 
and learn how to properly implement faker in your code.
Create an empty list called users. Tip: It should be a list of dictionaries.
Create a function that adds new dictionaries to the users list. 
Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.
'''

from faker import Faker

fake = Faker()
users = []

def add_user(users_list):
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users_list.append(user)
    

for _ in range(10):  # Add 10 users
    add_user(users)

for user in users:
    print(user)
