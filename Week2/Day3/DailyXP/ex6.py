'''
Exercise 6 : Birthday and minutes
Instructions
Create a function that accepts a birthdate as an argument (in the format of your choice), 
then displays a message stating how many minutes the user lived in his life.

'''

from datetime import datetime

def calculate_minutes_lived(birthdate_str, date_format="%d-%m-%Y"):

    birthdate = datetime.strptime(birthdate_str, date_format)
    now = datetime.now()
    time_lived = now - birthdate
    minutes_lived = int(time_lived.total_seconds() / 60)
    print(f"You have lived for {minutes_lived:,} minutes.")

# Example usage
calculate_minutes_lived("14-11-1999")
