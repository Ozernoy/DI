'''
Exercise 5: Longest word without a specific character
Instructions
Keep asking the user to input the longest sentence they can without the character “A”.
Each time a user successfully sets a new longest sentence, print a congratulations message.
'''


string = ''
record = 0
while "A" not in string and "a" not in string:
    string = str(input('Input ypur string: '))
    if len(string) > record: 
        record = len(string)
        print(f'Congratulations! Your new record {record}')
    else:
        print('Keep trying. You can do better.')
else:
    print(f'You loose! Your record was {record}')