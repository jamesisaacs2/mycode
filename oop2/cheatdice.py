#!/usr/bin/python3
"""Player - Class model
   Cheat_Swapper(Player) - Subclass model
   Cheat_Loaded_Dice(Player) - Subclass model"""

# standard library
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = [] # clears current dice
        for i in range(3):  # make 3 rolls
            self.dice.append(randint(1,6))   # 1 to 6 inclusive

    def get_dice(self): # returns the dice rolls
        return self.dice

# allows user to turn their last roll into a 6
class Cheat_Swapper(Player):  # inheritance of Player
    def cheat(self):
        self.dice[-1] = 6

# allows user to increase all rolls if they were less than a 6
class Cheat_Loaded_Dice(Player): # inheritance of Player
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1

# if total dice is under 9, get a re-roll
class Cheat_Mulligan(Player):
    def cheat(self):
       if sum(self.dice) <= 9:
           self.dice = []
           for i in range(3):
              self.dice.append(random.randint(1,6))

# add an extra dice roll
class Cheat_Extra_Die(Player):
    def cheat(self):
        self.dice.append(random.randint(1,6))

# first die roll is lucky and can't roll under a 3
class Cheat_Lucky_Die(Player):
    def cheat(self):
        if self.dice[0] < 3:
           self.dice[0]= random.randint(3,6)

# switch other player's dice with dice that can't roll above a 3
class Cheat_Saboteur(Player):
    def cheat(self, other_player):
        other_player.dice = [random.randint(1,3) for i in range(3)]
                        # ^ this is a list comprehension;
                        # a handy way to generate list contents
                        # in one line of code

