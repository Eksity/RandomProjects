import random
import pandas as pd
class Deck:
    def __init__(self, size):
        self.size = size
        self.cardlist = self.draw(size)
    
    def __str__(self):
        return f"{self.cardlist}"

    def toexcel(self):
        hearts = []
        spades = []
        clubs = []
        diamonds = []
        for i in self.cardlist:
            x = i.split(" ")
            match x[1]:
                case "Spades":
                    spades.append(x[0])
                case "Hearts":
                    hearts.append(x[0])
                case "Clubs":
                    clubs.append(x[0])
                case "Diamonds":
                    diamonds.append(x[0])
        spades.insert(0, len(spades))
        hearts.insert(0, len(hearts))
        clubs.insert(0, len(clubs))
        diamonds.insert(0, len(diamonds))
        for i in range(self.size):
            while len(hearts) != len(spades):
                if len(hearts) > len(spades):
                    spades.append("")
                elif len(spades) > len(hearts):
                    hearts.append("")
            while len(clubs) != len(spades):
                if len(clubs) > len(spades):
                    spades.append("")
                elif len(spades) > len(clubs):
                    clubs.append("")
            while len(diamonds) != len(spades):
                if len(diamonds) > len(spades):
                    spades.append("")
                elif len(spades) > len(diamonds):
                    diamonds.append("")

        data = {'Spades': spades, 'Hearts':hearts, 'Clubs':clubs, 'Diamonds':diamonds}
        df = pd.DataFrame(data)
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

x = Deck(52)
x.toexcel()
