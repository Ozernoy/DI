'''
Exercise 4 : Current Date
Instructions
Create a function that displays the current date.
Hint : Use the datetime module.
'''

import datetime

def display_current_date():
    current_date = datetime.date.today()
    print("Current date:", current_date)


display_current_date()  
