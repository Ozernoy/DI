'''
Part 1. Quiz
Class: A blueprint for creating objects, defining their attributes and behaviors.
Instance: A specific object created from a class.
Encapsulation: Hiding internal data and providing controlled access via methods.
Abstraction: Simplifying complex systems by showing only essential features and hiding details.
Inheritance: Mechanism where a class derives attributes and behaviors from another class.
Multiple Inheritance: A class inheriting from more than one parent class.
Polymorphism: Ability for different classes to be treated as instances of the same class through a common interface.
Method Resolution Order (MRO): The order in which Python looks for methods in a hierarchy of classes, especially in the context of multiple inheritance.

'''


'''
Part 2: Create a deck of cards class.

The Deck of cards class should NOT inherit from a Card class.

The requirements are as follows:

The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
The Deck class :
should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
'''

import random

# Card class
class Card:
    def __init__(self, suit: str, value: str) -> None:
        self.suit = suit
        self.value = value

    def __repr__(self) -> str:
        return f"{self.value} of {self.suit}"

# Deck class
class Deck:
    def __init__(self) -> None:
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]
    
    def shuffle(self) -> None:
        if len(self.cards) != 52:
            print("Incomplete deck! Restoring to full deck before shuffling.")
            self.__init__()  # Restore the deck to 52 cards
        random.shuffle(self.cards)

    def deal(self) -> Card:
        if len(self.cards) == 0:
            raise ValueError("All cards have been dealt!")
        return self.cards.pop()

# Example usage:
deck = Deck()
deck.shuffle()

# Dealing some cards
print(deck.deal())
print(deck.deal())

# Display remaining cards
print(f"Remaining cards in deck: {len(deck.cards)}")

for _ in range(len(deck.cards) + 1):
    print(deck.deal())
