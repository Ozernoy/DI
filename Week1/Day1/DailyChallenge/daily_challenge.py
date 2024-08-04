'''
Instructions
Using the input function, ask the user for a string. The string must be 10 characters long.
If it’s less than 10 characters, print a message which states “string not long enough”.
If it’s more than 10 characters, print a message which states “string too long”.
If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

Then, print the first and last characters of the given text.

Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
The user enters "HelloWorld"
Then, you have to construct the string character by character
H
He
Hel
... etc
HelloWorld


4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

Hlrolelwod
'''

import random

string = str(input('Input string: '))

if len(string) < 10:
    print('string not long enough')
elif len(string) > 10:
    print('string too long')
else:
    print('perfect string')

    print("First character:", string[0])
    print("Last character:", string[-1])

    for i in range(1, len(string) + 1):
        print(string[:i])

    str_list = list(string)
    random.shuffle(str_list)
    shuffled_string = ''.join(str_list)
    print('Here\'s the shuffled string:', shuffled_string)
