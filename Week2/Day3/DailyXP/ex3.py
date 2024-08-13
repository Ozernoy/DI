'''
🌟 Exercise 3: String module
Instructions
Generate random String of length 5
Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
Hint: use the string module
'''

import string
import random

def generate_random_string(length=5):
    letters = string.ascii_letters  # This includes both uppercase and lowercase letters
    random_string = ''.join(random.choice(letters) for _ in range(length)) # join gets a generator expression as an input and turns it into a sting
    return random_string


random_string = generate_random_string()
print(random_string) 
