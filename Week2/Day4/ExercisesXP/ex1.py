'''
🌟 Exercise 1 – Random Sentence Generator
Instructions
Description: In this exercise we will create a random sentence generator. 
We will do this by asking the user how long the sentence should be and then printing the generated sentence.

Hint : The generated sentences do not have to make sense.

Download this word list

Save it in your development directory.

Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. 
What is the correct data type to store the words?

Create another function called get_random_sentence which takes a single parameter called length. 
The length parameter will be used to determine how many words the sentence should have. The function should:
use the words list to get your random words.
the amount of words should be the value of the length parameter.

Take the random words and create a sentence (using a python method), the sentence should be lower case.

Create a function called main which will:

Print a message explaining what the program does.

Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20.
 Validate your data and test your validation!
If the user inputs incorrect data, print an error message and end the program.
If the user inputs correct data, run your code.
'''

import random
import os

class Ran_sen_gen:

    def __init__(self):
        pass
    
    def get_words_from_file(self, path):
        ''' 
        That's the only way of openning file that worked for me.
        Others raised an erro FileNotFount
        '''
        # Get the directory where the script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Build the full path to 'sowpods.txt'
        file_path = os.path.join(script_dir, 'sowpods.txt')
        with open(file_path, 'r') as file:
            words = file.readlines()
        return [word.strip() for word in words if word.strip()]  # Clean up the words. word.strip() may produce some empty strings, so we clean them

    def get_random_sentence(self, length):
        words = self.get_words_from_file('sowpods.txt') 
        if length > len(words):
            raise ValueError("Requested sentence length exceeds the number of available words.")
        return random.sample(words, length)
    
    def input_validation(self):
        while True:
            try:
                length = int(input('Please provide the desired length between 2 and 20: '))
                if 2 <= length <= 20:
                    return length
                else:
                    raise ValueError('Input must be between 2 and 20')
            except ValueError as e:
                print(f'Invalid input: {e}. Please try again')


    def main(self, path='Week2/Day4/ExercisesXP/sowpods.txt'):
        print('This program takes the source file with words and make of it a sentence with k random words')
        length = self.input_validation()
        sentence = ' '.join(self.get_random_sentence(length)).lower()
        print(f"Generated sentence: {sentence}")


RSC1 = Ran_sen_gen()
RSC1.main()