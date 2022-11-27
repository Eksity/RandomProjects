import random
import pandas as pd
class Deck:
    def __init__(self, size):
        self.size = size
        self.cardlist = self.draw(size)
    
    def __str__(self):
        return f"{self.cardlist}"

    def toexcel(self):
        valueslist = []
        suitslist = []
        for i in self.cardlist:
            x = i.split(" ")
            valueslist.append(x[0])
            suitslist.append(x[1])
        df = pd.DataFrame({'values': valueslist, 'suits':suitslist})
        df.to_excel("~/Desktop/foo.xlsx")
            

    @classmethod
    def draw(cls, num):
        cardslist = set()
        suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] 
        if 0 < num <= (len(suits)*len(values)):
            while len(cardslist) < int(num):
                cardslist.add(f'{random.choice(values)} {random.choice(suits)}')
        else:
            raise ValueError("Invalid number of cards")
        return cardslist

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 1:
            raise ValueError("Deck too small")
        self._size = size

x = Deck(25)
x.toexcel()
print(x)