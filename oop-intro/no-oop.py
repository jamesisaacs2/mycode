#!/usr/bin/env python3

# standard library
import random

def main():
    """run time code"""

    # create lists to store the scores
    player1_dice = []
    player2_dice = []

    for i in range(3):
      player1_dice.append(random.randint(1,6)) # 1 to 6 inclusive
      player2_dice.append(random.randint(1,6)) # 1 to 6 inclusive

    print("Player 1 rolled", player1_dice)
    print("Player 2 rolled", player2_dice)

    # determine which player won
    if sum(player1_dice) == sum(player2_dice):
      print("Draw")
    elif sum(player1_dice) > sum(player2_dice):
      print("Player 1 wins")
    else:
      print("Player 2 wins")
      
if __name__ == "__main__":
    main()

