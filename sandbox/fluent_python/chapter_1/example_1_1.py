'''A Pythonic card deck'''

# Attributes-only class using namedtuple
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
ace_of_spades = Card('A', 'spades')
print(ace_of_spades)

# Deck class
class Deck:
    ranks = [str(k) for k in range(2, 11)] + list('JQKA')
    suits = 'spades clubs diamonds hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks] 

    # Allow the class to support basic Python constructs e.g. iteration, collections by defining __len__, __getitem__    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
from random import choice
deck = Deck()
print(deck[0])
print(deck[-1])
print(deck[:4])
print(choice(deck))
for card in reversed(deck):
    print(card)

# Sort cards in strength order, e.g.
# strength(Card('2', 'clubs')) = 0, strength(Card('2', 'diamonds')) = 1, strength(Card('2', 'hearts')) = 2, ...
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def strength(card: Card):
    rank_value = Deck.ranks.index(card.rank)
    return (4 * rank_value) + suit_values[card.suit]

for card in sorted(deck, key=strength):
    print(f'{card} has {strength(card)} strength')
