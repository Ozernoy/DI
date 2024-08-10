'''

Challenge 2 : Longest Word
Instructions
Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).
'''

def longest_word(sentence):
    words = sentence.split()
    
    # Find the longest word using max with a key based on the length of the word
    longest = max(words, key=len)
    
    return longest


print(longest_word("Margaret's toy is a pretty doll."))  
print(longest_word("A thing of beauty is a joy forever."))  
print(longest_word("Forgetfulness is by all means powerless!"))  
