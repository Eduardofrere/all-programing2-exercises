import random
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


    
class FrenchDeck:
    ranks= ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    suits=["hearts","diamonds","spades","clubs"]

    def __init__(self,):
        self._cards=[Card(suit,rank)for suit in FrenchDeck.suits for rank in FrenchDeck.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,index):
        return self._cards[index]
    
    def __setitem__(self, index, value):
        if not isinstance(value,Card):
            raise TypeError("only cards can be put in deck")
        self._cards[index]=value

deck = FrenchDeck()
print(random.choice(deck)) # Draw a random card
print(deck[0]) # Draw the first card
for card in deck:
    print(card)
random.shuffle(deck)
print(deck[0]) # Draw the first card after shuffling
