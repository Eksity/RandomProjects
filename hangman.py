import random
import sys
import os

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


word_file = "/usr/share/dict/words"
with open(word_file) as file:
    words = file.read().splitlines()

class Hangman:
    def __init__(self, word):
        self.word = word
        self.blanks = []
        for i in range(len(word)):
            self.blanks.append("_")
        self.strikes = 0
        self.guessed = []
        self.solved = False
        self.message = ""
        self.end = False
    
    def __str__(self):
        return " ".join(self.blanks)

    def guess(self, letter):
        if letter in self.guessed:
            self.message = "Letter already guessed!"
        else:
            tempword = list(self.word)
            if letter in self.word:
                while True:
                    if letter in tempword:
                        ind = tempword.index(letter)
                        self.blanks[ind] = letter
                        tempword[ind] = ""
                    else:
                        break
            elif letter not in self.word:
                self.strikes += 1
            self.guessed.append(letter)
            if self.strikes >= 6:
                hang.message = f"You lose! the word was {self.word}"
                hang.end = True
            elif "_" not in self.blanks:
                hang.message = f"You win! the word was {self.word}."
                hang.end = True

def lettercheck(letter):
    if len(letter) != 1:
        return False
    elif letter not in 'abcdefghijklmnopqrstuvwxyz':
        return False
    else:
        return True
        

if __name__ == "__main__":
    hang = Hangman(random.choice(words))
    while True:
        os.system('cls' if sys.platform == 'win32' else 'clear')
        if hang.message:
            if hang.end:
                print(HANGMANPICS[hang.strikes])
                sys.exit(hang.message)
            print(hang.message)
            hang.message = ""
        print(HANGMANPICS[hang.strikes])
        print(f"{hang}\n")
        print("letters guessed: " + ", ".join(hang.guessed) + "\n")
        lett = input("Guess: ")
        if not lettercheck(lett):
            continue
        hang.guess(lett)
        