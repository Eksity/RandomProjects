import pandas as pd
import openpyxl
import random
class test:
    def __init__(self, card, suit):
        self.card = card
        self.suit = suit
        
    
    def __str__(self):
        aliass = {"A":"Ace", "J":"Jack", "Q":"Queen", "K":"King", '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten'}
        return(f"Your card is the {aliass[self.card]} of {self.suit}")

    @property
    def card(self):
        return self._card
    
    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        if suit not in suits:
            raise ValueError("suit not valid")
        self._suit = suit

    @card.setter
    def card(self, card):
        cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        if card not in cards:
            raise ValueError("card not valid")
        self._card = card

def main():
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    randomcard = test(random.choice(cards), random.choice(suits))
    print(randomcard.suit)
    #df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
        #index=['one', 'two', 'three'], columns=['a', 'b', 'c'])

if __name__=="__main__":
    main()