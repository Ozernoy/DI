'''
Part I
First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

Create a class called Text that takes a string as an argument and store the text in a attribute.
Hint: You need to manually copy-paste the text, straight into the code

Implement the following methods:
a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
a method that returns the most common word in the text.
a method that returns a list of all the unique words in the text.


Part II
Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

Implement a classmethod that returns a Text instance but with a text file:

    >>> Text.from_file('the_stranger.txt')
Hint: You need to open and read the text from the text file.


Now, use the provided the_stranger.txt file and try using the class you created above.



Bonus:
Create a class called TextModification that inherits from Text.

Implement the following methods:
a method that returns the text without any punctuation.
a method that returns the text without any english stop-words (check out what this is !!).
a method that returns the text without any special characters.
Note: Instead of creating a child class, you could also implements those methods as static methods in the Text class.

Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)
'''

class Text:
    def __init__(self, content):
        self.content = content.lower()  

    def word_frequency(self, word):
        word = word.lower()
        words = self.content.split()
        frequency = words.count(word)
        if frequency == 0:
            return f"The word '{word}' does not appear in the text."
        return frequency

    def most_common_word(self):
        words = self.content.split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1 # We use get to safely check if word in the dict, if not we add it with default value 0
        most_common = max(word_count, key=word_count.get)
        return most_common

    def unique_words(self):
        words = self.content.split()
        unique_words = set(words)
        return list(unique_words)

    @classmethod  # We can apply this method straight to class Text, as we do it below
    def from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return cls(content)  # Create an instance of Text with the file content


text_input_instance = Text('A good book would sometimes cost as much as a good house.')
print(f"Frequency of 'book': {text_input_instance.word_frequency('book')}")
print(f"Most common word: {text_input_instance.most_common_word()}")
print(f"Unique words: {text_input_instance.unique_words()}")


text_file_instance = Text.from_file(r'Week2\Day4\DailyChallenge\the_stranger.txt') # Finaly found how to open files without os module 
print(f"Frequency of 'the': {text_file_instance.word_frequency('the')}")
print(f"Most common word: {text_file_instance.most_common_word()}")
# print(f"Unique words: {text_file_instance.unique_words()}")
