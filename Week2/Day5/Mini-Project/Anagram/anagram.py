'''


'''

from anagram_checker import AnagramChecker

class anagram:
    def __init__(self) -> None:
        pass

    @staticmethod
    def run():
        ac1 = AnagramChecker()
        input_str = input('Write a word for search of anagrams: ')
        word = ac1.word_cleaning(input_str)
        print(f'YOUR WORD :”{word}”')
        if ac1.word_validation(word):
            print('this is a valid English word.')
            combinations = ac1.get_combinations(word)
            anagram = ac1.get_anagrams(combinations)
            print(f'Anagrams for your word: {", ".join(anagram)}')


anagram.run()