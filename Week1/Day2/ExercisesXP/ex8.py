'''
Exercise 8: Who ordered a pizza ?
Instructions
Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
As they enter each topping, print a message saying you’ll add that topping to their pizza.
Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

'''
price = 10
t_list = []

print('What toppings do you want to add? Write one after another and press enter. ')
inp_str = input()

while inp_str.lower() != 'quit':
    price += 2.5
    t_list.append(inp_str)
    print(f'We will add {inp_str} to your pizza.')
    inp_str = input()

if t_list:  # Check on emptiness
    toppings = ', '.join(t_list)
    print(f'Toppings you\'ve chosen: {toppings}. Your final price: ${price:.2f}')
else:
    print(f'You haven\'t added any toppings. Your final price: ${price:.2f}')
