'''
Exercise 9 : Random number
Instructions
Ask the user to input a number from 1 to 9 (including).
Get a random number between 1 and 9. Hint: random module.
If the user guesses the correct number print a message that says Winner.
If the user guesses the wrong number print a message that says better luck next time.
Bonus: use a loop that allows the user to keep guessing until they want to quit.
Bonus 2: on exiting the loop tally up and display total games won and lost.
'''
import random



random_num = random.randint(1, 9)
print(random_num)
while True: # Game
    while True: # Input
        num = int(input('Input a number from 1 to 9 (including) or 0 to quit: '))
        if 1 <= num <= 9:
            break
        elif num == 0:
            quit()
        else:
            print('Incorrect input')
    if num == random_num:
        print('Winner!')
    else:
        print('Better luck next time!')