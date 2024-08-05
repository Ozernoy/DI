'''
Challenge 2
Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
Examples

user's word : "ppoeemm" ➞ "poem"

user's word : "wiiiinnnnd" ➞ "wind"

user's word : "ttiiitllleeee" ➞ "title"

user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
'''

word = 'ppoeemm'  # input("Enter a word: ")

word_cleaned = []

for i in range(len(word)):
    # If it's the first character or different from the previous character, add it to the cleaned list
    if i == 0 or word[i] != word[i - 1]:
        word_cleaned.append(word[i])


cleaned_word = ''.join(word_cleaned)
print(cleaned_word)
