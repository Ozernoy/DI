'''
Exercise 5: The Alphabet
Instructions
Create a string of all the letters in the alphabet
Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.

'''
import string

ab = string.ascii_lowercase
vowels = "aeiou"

for ch in ab:
    if ch in vowels:
        print(f'{ch} is a vowel!')
    else:
        print(f'{ch} is a consonant!')