import collections # we import this so that we can access the namedtuple datatype.
from random import choice # choice will allow us to select a random card from the deck

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA') # Here we list all the possible rank choices
    suits = 'spades diamonds clubs hearts'.split() # Here we list all the possible suit choices

    # This list comprehension iterates over the ranks and suits to create all possible combinations (52 cards)
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks] 
    
    # Here we are able to determine the length of the deck, which is necessary for the next method
    def __len__(self):
        return len(self._cards)

    # Here we can call a specific card by its index value
    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck() # Calling our function to create a deck

print(choice(deck)) # Choosing a card at random