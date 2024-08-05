'''
Exercise 9: Cinemax
Instructions
A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.

Ask a family the age of each person who wants a ticket.

Store the total cost of all the family’s tickets and print it out.

A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
At the end, print the final list.

'''


names = ['Mike', 'John', 'Jennie', 'Mark', 'Michael', 'Sophie']
price = 0
final_names = []

for name in names:
    while True:  # Loop until valid input is provided
        try:
            inp_age = int(input(f'{name}, what\'s your age? '))
            break  # Exit the loop if input is valid
        except ValueError:
            print(f"Invalid input for {name}. Please enter a valid age.")

    if 16 < inp_age < 21:
        print(f"Sorry, {name}, you are not allowed to watch this movie.")
        continue  # The end of the story for {name}. We do not go further with them
    
    final_names.append(name)  # Add name to the final list if they are allowed

    if inp_age <= 3:
        pass
    elif inp_age <= 12:
        price += 10
    else:
        price += 15

print(f"Total price for is: ${price}")
print(f"Final list of allowed viewers: {', '.join(final_names)}")



