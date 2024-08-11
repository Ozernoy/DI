'''
Exercise 4 : Disney characters
Instructions
Use this list :

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
Analyse these results :

#1/

>>> print(disney_users_A)
{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

#2/

>>> print(disney_users_B)
{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

#3/ 

>>> print(disney_users_C)
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
Only recreate the 1st result for:
The characters, which names contain the letter “i”.
The characters, which names start with the letter “m” or “p”.

'''

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# 1. Recreate the first result
disney_users_A = {}
for i, el in enumerate(users):
    disney_users_A[el] = i
print(disney_users_A)  

# 2. Recreate the second result
disney_users_B = {}
for i, el in enumerate(users):
    disney_users_B[i] = el
print(disney_users_B) 

# 3. Recreate the third result (sorted alphabetically by name)
disney_users_C = {el: i for i, el in enumerate(sorted(users))}
print(disney_users_C) 

# Only recreate the 1st result for names containing the letter “i”
disney_users_A_1 = {key: value for key, value in disney_users_A.items() if 'i' in key.lower()}
print(disney_users_A_1) 

# Only recreate the 1st result for names starting with “m” or “p”
disney_users_A_2 = {key: value for key, value in disney_users_A.items() if key.lower().startswith(('m', 'p'))}
print(disney_users_A_2) 
