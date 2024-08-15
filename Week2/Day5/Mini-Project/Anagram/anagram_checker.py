import itertools

class AnagramChecker:

    def __init__(self):
        with open(r'Week2\Day5\Mini-Project\Anagram\sowpods.txt', "r+") as file:
            self.content = file.read().upper().split('\n')
    
    # Check if word is valid and return it in the correct format
   
    def word_validation(self, word): 
        
        if len(word.split()) != 1:
            raise ValueError('More than one word.')
        
        if not word.isalpha():
            raise ValueError('Not all symbols alphabetical')
        return True
    

    def word_cleaning(self, word):
        return word.strip().upper()

    # Get all the combinations (permutations) with symbols of original word
    def get_combinations(self, word): 
        word_list = list(word)
        permutations = list(itertools.permutations(word_list)) # it returns a list of tuples
        combinations = [''.join(p) for p in permutations if ''.join(p) != word] #unite tuples into words and drop the original word
        return combinations

    # Get all the anagrams
    def get_anagrams(self, combinations,):
        result_list = [el for el in combinations if el in self.content]
        return result_list

