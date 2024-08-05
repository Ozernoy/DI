'''
Exercise 1 : Favorite Numbers
Instructions
Create a set called my_fav_numbers with all your favorites numbers.
Add two new numbers to the set.
Remove the last number.
Create a set called friend_fav_numbers with your friend’s favorites numbers.
Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
'''

my_fav_numbers = {2, 13, 42}
print(my_fav_numbers)
my_fav_numbers.update([5, 6])
print(my_fav_numbers)
my_fav_numbers.remove(6)
print(my_fav_numbers)
friend_fav_numbers = {420, 1337, 2007}
print(friend_fav_numbers)
my_fav_numbers.update(friend_fav_numbers)
our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)
