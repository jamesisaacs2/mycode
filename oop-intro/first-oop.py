#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Creating a simple dice program utilizing classes."""

# standard library
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    # a function defined within a class is a "method"
    def roll(self):
        self.dice = [] # clears current dice
        for i in range(3):  # make 3 rolls
            self.dice.append(randint(1,6))   # 1 to 6 inclusive

    # a function defined within a class is a "method"
    def get_dice(self): # returns the dice rolls
        return self.dice

def main():
    """called at run time"""

    ## create our player objects
    player1 = Player()
    player2 = Player()

    # player objects can use their method "roll"
    player1.roll()
    player2.roll()

    # the f-string is simply a "fill in the {} with the value inside"
    print(f"Player 1 rolled {player1.get_dice()}")
    print(f"Player 2 rolled {player2.get_dice()}")

    # determine which player won
    if sum(player1.get_dice()) == sum(player2.get_dice()):
        print("Draw!")
    elif sum(player1.get_dice()) > sum(player2.get_dice()):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


if __name__ == "__main__":
    main()

