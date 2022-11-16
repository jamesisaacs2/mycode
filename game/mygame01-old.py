#!/usr/bin/python3
"""Simple RPG game framework using dictionaries"""

# import os to clear terminal screen
# import random for randomization of actions
import os
import random

# set default starting state(s)
run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False

# set global starting character properties
# HP is hitpoints
HP = 100
# HPMAX are max hitpoints
HPMAX = 100
# attack
ATK = 3

# set starting inventory
potion = 1  # +25 HP
elixir = 0  # +67 HP
gold = 10

# set starting location
x = 0
y = 0

grid = [
    # x = 0     x = 1     x = 2    x = 3     x = 4     x = 5       x = 6
    ["plains", "forest", "road",  "plains", "forest", "mountain", "cave"],      # y = 0
    ["forest", "road",   "road",  "forest", "forest", "hills",    "mountain"],  # y = 1
    ["forest", "fields", "road",  "plains", "hills",  "forest",   "hills"],     # y = 2
    ["forest", "mayor",  "town",  "shop",   "fields", "forest",   "hills"],     # y = 3
    ["plains", "forest", "road",  "hills",  "plains", "hills",    "mountain"],  # y = 4
    ["plains", "fields", "house", "plains", "hills",  "mountain", "mountain"]   # y = 5
]

# set map outer limits
x_len = len(grid[0]) - 1
y_len = len(grid) - 1

# define the geography and enemies by geo
geo = {
    "plains": {
        "type": "PLAINS",
        "enemy": True},
    "forest": {
        "type": "FOREST",
        "enemy": True},
    "fields": {
        "type": "FIELDS",
        "enemy": True},
    "bridge": {
        "type": "BRIDGE",
        "enemy": True},
    "town": {
        "type": "TOWN",
        "enemy": True},
    "shop": {
        "type": "SHOP",
        "enemy": True},
    "mayor": {
        "type": "MAYOR",
        "enemy": True},
    "cave": {
        "type": "CAVE",
        "enemy": True},
    "mountain": {
        "type": "MOUNTAIN",
        "enemy": True},
    "hills": {
        "type": "HILLS",
        "enemy": True},
    "road": {
        "type": "ROAD",
        "enemy": True}
}

# list of possible "routine" enemies (not boss)
enemies_list = ["Goblin", "Troll", "Bandits", "Witch", "Ogre", "Orc", "Quicksand"]

# monster characteristics.
# dragon is boss
monsters = {
    "Goblin": {
        "hitpoints": 15,
        "attack": 3,
        "gold": 11},
    "Troll": {
        "hitpoints": 45,
        "attack": 8,
        "gold": 23},
    "Bandits": {
        "hitpoints": 35,
        "attack": 5,
        "gold": 18},
    "Witch": {
        "hitpoints": 20,
        "attack": 6,
        "gold": 15},
    "Ogre": {
        "hitpoints": 45,
        "attack": 9,
        "gold": 19},
    "Orc": {
        "hitpoints": 35,
        "attack": 8,
        "gold": 14},
    "Quicksand": {
        "hitpoints": 20,
        "attack": 2,
        "gold": 22},
    "Dragon": {
        "hitpoints": 100,
        "attack": 13,
        "gold": 222}
}


# clears screen in terminal as game runs
def reset_display():
    os.system("cls")


# injects visual breaks for better visuals in CLI
def draw_one():
    print("T====XxXx=======OoO=======xXxX====T")


def draw_two():
    print("X======oOOo=====xXx=====oOOo======X")


# records game progress
def save():
    # attributes to record / save
    attributes = [
        name,
        str(HP),
        str(ATK),
        str(potion),
        str(elixir),
        str(gold),
        str(x),
        str(y),
        str(key),
    ]

    # using open / close - can't remember the other method right now
    file = open("history.txt", "w")

    # write to file
    for item in attributes:
        file.write(item + "\n")
    # close file
    file.close()


# heal method, to use elixirs and restore hitpoints
def heal(plus_up):
    global HP
    if HP + plus_up < HPMAX:
        HP += plus_up
    else:
        HP = HPMAX
    print(f"You've been healed! and are now at {str(HP)} hitpoints")


# def battle method
def battle():
    # set global vars
    global fight, play, run, HP, potion, elixir, gold, boss

    # set boss condition, designate Dragon as boss
    if not boss:
        enemy = random.choice(enemies_list)
    else:
        enemy = "Dragon"
    hp = monsters[enemy]["hitpoints"]
    hpmax = hp
    atk = monsters[enemy]["attack"]
    gld = monsters[enemy]["gold"]

    # set fight sequence and conditions
    while fight:
        reset_display()
        draw_one()
        print(f"Show your mettle, defeat the {enemy}!")
        draw_two()
        print(f"{enemy}'s hitpoints are: {str(hp)} of {str(hpmax)}")
        print(f"Your hitpoints are: {str(HP)} of {str(HPMAX)} total")
        print(f"Potions: {str(potion)}")
        print(f"Elixir: {str(elixir)}")
        draw_one()
        print(f"1 - Attack!")
        if potion >= 1:
            print(f"2 - Take potion (+25 HP)")
        if elixir >= 1:
            print(f"3 - Take elixir (+67 HP) - {name} needs real healing!")
        draw_two()

        select = input("> ")

        if select == "1":
            hp -= ATK
            print(f"{name} damaged the {enemy} by {str(ATK)} points")
            if hp > 0:
                HP -= atk
                print(f"The {enemy} damaged {name} by {str(atk)} points")
            print("Hit enter to continue")
            input("> ")

        elif select == "2":
            if potion >= 1:
                potion -= 1
                heal(25)
                HP -= atk
                print(f"The {enemy} damaged {name} by {str(atk)} points")
            else:
                print(f"{name} ain't got no potions left. So sad, looks like you're SOL...")
            print("Hit enter to continue")
            input("> ")

        elif select == "3":
            if elixir >= 1:
                elixir -= 1
                heal(67)
                HP -= atk
                print(f"The {enemy} damaged {name} by {str(atk)} points")
            else:
                print(f"{name} ain't got no elixir left. So sorry, try a potion instead...?")
            print("Hit enter to continue")
            input("> ")

        if HP <= 0:
            print(f"The {enemy} defeated you, {name}...  Say it ain't so...")
            draw_one()
            fight = False
            play = False
            run = False
            print(f"Bummer {name} -- GAME is OVER!")
            draw_two()
            input("> ")

        if hp <= 0:
            print(f"Hold on to your hats:  {name} has, somehow, miraculously defeated the {enemy}!")
            draw_one()
            fight = False
            gold += gld
            print(f"You've found {str(gld)} gold!")
            if random.randint(0, 100) < 25:
                potion += 1
                print(f"You've found a potion!")
            if enemy == "Dragon":
                draw_two()
                print(f"It can't be... {name} has WON -- Congratulations!")
                boss = False
                play = False
                run = False
            print("Hit enter to continue")
            input("> ")
            reset_display()


# def shop, increase inventory
def shop():
    global buy, gold, potion, elixir, ATK

    while buy:
        reset_display()
        draw_two()
        print("Welcome to Yitzchak General Store!")
        draw_one()
        print(f"Gold: {str(gold)}")
        print(f"Potions: {str(potion)}")
        print(f"Elixirs: {str(elixir)}")
        print(f"Attack: {str(ATK)}")
        draw_one()
        print("1 - Buy a potion (+25 HP) - 5 GOLD")
        print("2 - Buy an elixir (+67 HP) - 10 GOLD")
        print("3 - Upgrade your weapons (+3 ATK) - 8 GOLD")
        print("4 - Leave store")
        draw_two()

        select = input("> ")

        if select == "1":
            if gold >= 5:
                potion += 1
                gold -= 5
                print("You got a potion!")
            else:
                print(f"What are you thinking?  You haven't enough gold!  May I suggest going elsewhere...")
            print("Hit enter to continue")
            input("> ")
        elif select == "2":
            if gold >= 10:
                elixir += 1
                gold -= 10
                print("Good choice, you got an elixir!")
            else:
                print(f"With no money, are you for real?  May I suggest a potion perhaps...")
            print("Hit enter to continue")
            input("> ")
        elif select == "3":
            if gold >= 8:
                ATK += 3
                gold -= 8
                print(f"Your attack just improved by +3, it's now at {str(ATK)}!")
            print("Hit enter to continue")
            input("> ")
        elif select == "4":
            buy = False


# def mayor, for mayor conversation
def mayor():
    global speak, key

    while speak:
        reset_display()
        draw_one()
        print(f"Hello, hopeful hero, {name}!")
        print("I see you are here, perhaps thinking you are ready to defeat the "
              "greatest enemy you have ever faced...")
        if ATK < 18:
            print(f"Alas, you are not.  Keep training and return when you are ready!")
            key = False
        else:
            print("Your time has come, young warrior, you are now ready. "
                  "Take this key to enter the beast's lair."
                  "And do be careful not to... lose, let us say.")
            key = True

        draw_one()
        print("1 - Leave")
        draw_two()

        select = input("> ")
        if select == "1":
            speak = False


# def cave, for boss fight with dragon
def cave():
    global boss, key, fight

    while boss:
        reset_display()
        draw_two()
        print("You have found the beast's lair... Now what will you do?")
        print("Do you have the key?")
        draw_one()
        if key:
            print("1 - Use key to enter (at your own peril!)")
        else:
            print("2 - I still need to get it, I'll be back")
        draw_two()

        select = input("> ")
        if select == "1":
            if key:
                fight = True
                battle()  # game on!
        elif select == "2":
            boss = False


# set while run
while run:
    while menu:
        draw_one()
        print("Welcome! Make your choice below...")
        draw_two()
        print("1 - New game")
        print("2 - Load game")
        print("3 - Rules")
        print("4 - Quit game")

        if rules:
            print("Direct from the Creator, these are the rules:\n")
            print("1. Roam around the map to find enemies to defeat\n"
                  "--> That's how you get gold!  And you need gold to upgrade\n"
                  "your weapons and buy potions and elixirs to heal yourself...\n"
                  "(there ain't no doctors or hospitals in these here parts...\n\n"
                  "2. Once you have defeated some enemies (and gotten their gold!),\n"
                  "find the Shop to upgrade your weapons.  If you stumble upon\n"
                  "the Town, the Shop is sure to be nearby\n\n"
                  "3. Head over to see the Mayor, she holds the Key to enter\n"
                  "the lair of the beast that you must defeat!  If she won't give\n"
                  "the key yet, repeat steps 1 and 2 until she will...\n\n"
                  "4. Got the key from the Mayor?!  Now find the cave...\n"
                  "That's the abode of the mighty beast that you, oh warrior\n"
                  "will must defeat!\n\n"
                  "FAQ:  How do I win the game?\n"
                  "A:  Defeat the beast to win!  Read the Rules above...\n")
            rules = False
            choice = ""
            print("Hit enter to continue")
            input("> ")
        else:
            choice = input("> ")

        if choice == "1":
            reset_display()
            name = input("What's your name, mighty warrior, soon-to-be-wayward hero?")
            menu = False
            play = True
        elif choice == "2":
            try:
                save_file = open("history.txt", "r")
                play_history = save_file.readlines()
                if len(play_history) == 9:
                    name = play_history[0][:-1]
                    HP = int(play_history[1][:-1])
                    ATK = int(play_history[2][:-1])
                    potion = int(play_history[3][:-1])
                    elixir = int(play_history[4][:-1])
                    gold = int(play_history[5][:-1])
                    x = int(play_history[6][:-1])
                    y = int(play_history[7][:-1])
                    key = bool(play_history[8][:-1])
                    reset_display()
                    print(f"Welcome back, {name}!")
                    print("Hit enter to resume your game.")
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("The history file seems to be corrupted!")
                    input("> ")
            except OSError:
                print("No loadable game play history file!")
                input("> ")

        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play:
        # implements "autosave"
        save()
        reset_display()

        if not standing:
            if geo[grid[y][x]]["enemy"]:
                if random.randint(0, 100) > 50:
                    fight = True
                    battle()

        if play:
            draw_one()
            print("Your location: " + geo[grid[y][x]]["type"])
            draw_two()
            print("Name: " + name)
            print(f"HP: {str(HP)} of {str(HPMAX)} max")
            print(f"ATK: {str(ATK)}")
            print(f"Potions: {str(potion)}")
            print(f"Elixir: {str(elixir)}")
            print(f"Gold: {str(gold)}")
            print(f"Coordinates. x: {x}, y: {y}")
            draw_one()
            print("0 - Save and quit")
            if y > 0:
                print("1 - North")
            if x < x_len:
                print("2 - East")
            if y < y_len:
                print("3 - South")
            if x > 0:
                print("4 - West")
            if potion >= 1:
                print("5 - Take potion (+25 HP)")
            if elixir >= 1:
                print("6 - Take elixir (+67 HP)")
            if grid[y][x] == "shop" or grid[y][x] == "mayor" or grid[y][x] == "cave":
                print("7 - ENTER...")
            draw_two()

            action = input("> ")

            if action == "0":
                play = False
                menu = True
                save()
            elif action == "1":
                if y > 0:
                    y -= 1
                    standing = False
            elif action == "2":
                if x < x_len:
                    x += 1
                    standing = False
            elif action == "3":
                if y < y_len:
                    y += 1
                    standing = False
            elif action == "4":
                if x > 0:
                    x -= 1
                    standing = False
            elif action == "5":
                if potion > 0:
                    potion -= 1
                    heal(25)
                else:
                    print("Oops, no potions in your kitbag!")
                input("> ")
                standing = True
            elif action == "6":
                if elixir > 0:
                    elixir -= 1
                    heal(67)
                else:
                    print("You fumble and grope and -- DO-HHHH -- no elixirs are to be found in your bag!"
                          "Try a potion instead perhaps?")
                input("> ")
                standing = True
            elif action == "7":
                if grid[y][x] == "shop":
                    buy = True
                    shop()
                if grid[y][x] == "mayor":
                    speak = True
                    mayor()
                if grid[y][x] == "cave":
                    buy = True
                    cave()
            else:
                standing = True
