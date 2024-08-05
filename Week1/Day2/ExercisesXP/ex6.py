'''
Exercise 6 : While Loop
Instructions
Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
'''
name = input('What\'s your name? ')
while name != 'Danila':
    print('Try again')
    name = input()
else:
    print('You good')
