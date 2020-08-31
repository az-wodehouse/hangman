from random import choice
from dataclasses import dataclass

@dataclass
class State:
    word: list
    guessed: list
    wrong_left: int

try:
    with open('wordlist.txt') as f:
        WORDLIST = []
        for word in f:
            WORDLIST.append(word.lower().strip())
except FileNotFoundError:
    print("you need a file in the same directory called wordlist.txt, with the words allowed separated by newlines")

def hangman(wrong_allowed=5):
    def prettyprint():
        print()
        print(" ".join((x.upper() if x in game.guessed else "_") for x in game.word))
        print("already guessed: " + " ".join(game.guessed))
        print("remaining wrong guesses allowed: " + str(game.wrong_left))

    def take_input():
        print("what's your guess?")
        guess = input()
        guess = guess.lower()
        while not guess.isalpha() or len(guess) != 1 or guess in game.guessed:
            print("invalid guess, try again")
            guess = input()
            guess = guess.lower()
        game.guessed.append(guess)
        if guess not in game.word:
            game.wrong_left -= 1

    def win_check():
        return all(x in game.guessed for x in game.word)

    game = State(word=choice(WORDLIST), guessed=[], wrong_left=wrong_allowed)
    prettyprint()
    while game.wrong_left >= 0:
        take_input()
        prettyprint()
        if win_check():
            break
    else:
        print("Take the L, my guy. The word was: " + game.word)
        return
    print("You win!")

hangman()
