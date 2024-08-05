'''
Exercise 3: Working on a paragraph
Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
Paste it to your code, and store it in a variable.
Let’s analyze the paragraph. Print out a nicely formatted message saying:
How many characters it contains (this one is easy…).
How many sentences it contains.
How many words it contains.
How many unique words it contains.
Bonus: How many non-whitespace characters it contains.
Bonus: The average amount of words per sentence in the paragraph.
Bonus: the amount of non-unique words in the paragraph.
'''

paragraph = """“Well, Prince, so Genoa and Lucca are now just family estates of the Buonapartes. But I warn you, if you don’t tell me that this means war, if you still try to defend the infamies and horrors perpetrated by that Antichrist—I really believe he is Antichrist—I will have nothing more to do with you and you are no longer my friend, no longer my ‘faithful slave,’ as you call yourself! But how do you do? I see I have frightened you—sit down and tell me all the news.”

It was in July, 1805, and the speaker was the well-known Anna Pávlovna Schérer, maid of honor and favorite of the Empress Márya Fëdorovna. With these words she greeted Prince Vasíli Kurágin, a man of high rank and importance, who was the first to arrive at her reception. Anna Pávlovna had had a cough for some days. She was, as she said, suffering from la grippe; grippe being then a new word in St. Petersburg, used only by the elite.

All her invitations without exception, written in French, and delivered by a scarlet-liveried footman that morning, ran as follows:

“If you have nothing better to do, Count (or Prince), and if the prospect of spending an evening with a poor invalid is not too terrible, I shall be very charmed to see you tonight between 7 and 10—Annette Schérer.”"""

# Total character count
ch_count = len(paragraph)

# Sentence count
sent_count = paragraph.count('.') + paragraph.count('!') + paragraph.count('?')

# Word count
words = paragraph.split()
words_count = len(words)

# Clean the paragraph for unique word count
chars_to_remove = [',', '.', '!', "“", '(', ')', ':', '—', '”', ';']
paragraph_cleaned = paragraph.lower()
for char in chars_to_remove:
    paragraph_cleaned = paragraph_cleaned.replace(char, '')

unique_words = set(paragraph_cleaned.split())
unique_words_count = len(unique_words)

# Non-whitespace characters
non_whitespace_count = len(paragraph.replace(' ', '').replace('\n', ''))

# Average words per sentence
words_p_sent = words_count / sent_count

# Non-unique words count
non_unique_words_count = words_count - unique_words_count

# Output the results
print(f"Total characters: {ch_count}")
print(f"Total sentences: {sent_count}")
print(f"Total words: {words_count}")
print(f"Unique words: {unique_words_count}")
print(f"Non-whitespace characters: {non_whitespace_count}")
print(f"Average words per sentence: {words_p_sent:.2f}")
print(f"Non-unique words: {non_unique_words_count}")

