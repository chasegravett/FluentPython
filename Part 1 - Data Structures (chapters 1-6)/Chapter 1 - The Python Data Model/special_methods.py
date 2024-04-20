# The Python Data Model is the API we use to make our own objects 'play well' with the language features

# This chapter deals a lot with special methods, also called dunder methods. Denoted by double underscores around the method name

# A Pythonic Card Deck - simple but demonstrates the power of implementing 2 special methods (__getitem__ and __len__)
import collections

Card = collections.namedtuple('Card', ['suit', 'rank'])

# class Card:

#     def __init__(self, suit, rank):
#         self.suit = suit
#         self.rank = rank

#     def __str__(self):
#         return f"{self.rank} of {self.suit.title()}"

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')   # Concise way of doing something like "JQKA".split() AND list1 + list2 = list1.extend(list2)
    suits = 'spades clubs diamonds hearts'.split()

    def __init__(self):
        self._cards = [Card(suit, rank) for suit in self.suits 
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    # def __str__(self):
    #     output = ""
    #     for card in self._cards:
    #         output += str(card)
    #         output += "\n"
    #     return output
    

new_deck = FrenchDeck()

# Can now support len(new_deck), getting the nth card by new_deck[n]
print(new_deck[9::13]) # Prints all jacks

# Implementation of __getitem__ also means our deck object automatically supports slicing and iteration
for card in new_deck:
    print(f"{card[1]} of {card[0]}")
    

