'''
Exercise 6: Words and letters
Instructions
Ask a user for 7 words, store them in a list named words.
Ask the user for a single character, store it in a variable called letter.
Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.
'''
word_list = []
for _ in range(7):
    word = input('Input the word: ')
    word_list.append(word)

letter = input('Input the letter: ')

for word in word_list:
    position = word.find(letter)
    if position != -1:
        print(f'{letter} is found in {word} at position {position}')
    else:
        print(f'{letter} not found in word {word}')