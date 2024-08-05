'''
Exercise 4: Greatest Number
Instructions
Ask the user for 3 numbers and print the greatest number.
    Test Data
    Input the 1st number: 25
    Input the 2nd number: 78
    Input the 3rd number: 87

    The greatest number is: 87
'''

max_num = int(input('Input the 1 number '))
for i in range(2):
    num = int(input(f'Input the {i+2} number '))
    if num > max_num:
        max_num = num
print(f'The greatest number is: {max_num}')