'''
🌟 Exercise 1: Cats
Instructions
Using this class

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
Instantiate three Cat objects using the code provided above.
Outside of the class, create a function that finds the oldest cat and returns the cat.
Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

'''


class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

murzik_cat = Cat(cat_name='Murzik', cat_age=42)
pushok_cat = Cat(cat_name='Pushok', cat_age=26)
rizhik_cat = Cat(cat_name='Rizhik', cat_age=18)

def find_oldest_cat(*cats):
    oldest_cat = max(cats, key=lambda cat: cat.age)
    return oldest_cat

oldest_cat = find_oldest_cat(murzik_cat, pushok_cat, rizhik_cat)

# Print the result
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
