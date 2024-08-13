'''
Exercise 5 : Amount of time left until January 1st
Instructions
Create a function that displays the amount of time left from now until January 1st.
(Example: the 1st of January is in 10 days and 10:34:01hours).

'''

import datetime

def time_until_new_year():
    now = datetime.datetime.now()
    next_year = now.year + 1
    new_year = datetime.datetime(year=next_year, month=1, day=1)
    time_left = new_year - now
    
    days = time_left.days
    # with divmod() we can simultaneously calculate the quotient and the remainder
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"The 1st of January is in {days} days and {hours:02}:{minutes:02}:{seconds:02} hours.")

# Example usage
time_until_new_year()
