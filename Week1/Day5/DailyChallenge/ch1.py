'''

Challenge 1 : Sorting
Instructions
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Use List Comprehension
Example:

Suppose the following input is supplied to the program: without,hello,bag,world
Then, the output should be: bag,hello,without,world

'''

def sort_words(input_string):
    # Split the input string into a list of words, sort them, and join them back into a comma-separated string
    return ','.join(sorted([word for word in input_string.split(',')]))


input_string = "without,hello,bag,world"
print(sort_words(input_string))  