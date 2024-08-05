'''
Exercise 2 : List of integers
Instructions
Given a list of 10 integers to analyze. For example:

    [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
    [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
    [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
    [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
Store the list of numbers in a variable.
Print the following information:
a. The list of numbers – printed in a single line
b. The list of numbers – sorted in descending order (largest to smallest)
c. The sum of all the numbers
A list containing the first and the last numbers.
A list of all the numbers greater than 50.
A list of all the numbers smaller than 10.
A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
The numbers without any duplicates – also print how many numbers are in the new list.
The average of all the numbers.
The largest number.
10.The smallest number.
11.Bonus: Find the sum, average, largest and smallest number without using built in functions.
12.Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. 
Ask the user for an integer between -100 and 100 – repeat this question 10 times.
 Each number should be added into a variable that you created earlier.
13.Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
14.Bonus: Instead of always generating 10 integers, let the amount of integers also be random! 
Generate a random positive integer no smaller than 50.
15.Bonus: Will the code work when the number of random numbers is not equal to 10?

'''

import random

# Bonus 12: Ask the user for 10 numbers between -100 and 100
# numbers = []
# for i in range(10):
#     while True:
#         try:
#             num = int(input(f"Enter number {i+1} between -100 and 100: "))
#             if -100 <= num <= 100:
#                 numbers.append(num)
#                 break
#             else:
#                 print("Please enter a number between -100 and 100.")
#         except ValueError:
#             print("Please enter a valid integer.")

# Bonus 13: Generate 10 random integers between -100 and 100
# numbers = [random.randint(-100, 100) for _ in range(10)]

# Bonus 14: Generate a random number of integers (no smaller than 50)
list_size = random.randint(50, 100)  # Random number between 50 and 100
numbers = [random.randint(-100, 100) for _ in range(list_size)]

# a. Print the list of numbers
print("List of numbers:", numbers)

# b. Print the list sorted in descending order
sorted_numbers = sorted(numbers, reverse=True)
print("Sorted list in descending order:", sorted_numbers)

# c. Sum of all numbers
total_sum = sum(numbers)
print("Sum of all numbers:", total_sum)

# d. List containing the first and last numbers
first_and_last = [numbers[0], numbers[-1]]
print("First and last numbers:", first_and_last)

# e. List of all numbers greater than 50
greater_than_50 = [num for num in numbers if num > 50]
print("Numbers greater than 50:", greater_than_50)

# f. List of all numbers smaller than 10
smaller_than_10 = [num for num in numbers if num < 10]
print("Numbers smaller than 10:", smaller_than_10)

# g. List of all numbers squared
squared_numbers = [num ** 2 for num in numbers]
print("Squared numbers:", squared_numbers)

# h. Numbers without any duplicates
unique_numbers = list(set(numbers))
print("Unique numbers:", unique_numbers)
print("Number of unique numbers:", len(unique_numbers))

# i. Average of all numbers
average = total_sum / len(numbers)
print("Average of all numbers:", average)

# j. Largest number
largest = max(numbers)
print("Largest number:", largest)

# k. Smallest number
smallest = min(numbers)
print("Smallest number:", smallest)

# Bonus 11: Find sum, average, largest, and smallest without built-in functions
manual_sum = 0
manual_largest = numbers[0]
manual_smallest = numbers[0]

for num in numbers:
    manual_sum += num
    if num > manual_largest:
        manual_largest = num
    if num < manual_smallest:
        manual_smallest = num

manual_average = manual_sum / len(numbers)

print("Manual sum:", manual_sum)
print("Manual average:", manual_average)
print("Manual largest:", manual_largest)
print("Manual smallest:", manual_smallest)

# Bonus 15: Will the code work with random numbers not equal to 10?
# Yes, the code will still work because it does not rely on the list having exactly 10 elements.

