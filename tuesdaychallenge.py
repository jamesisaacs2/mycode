#!/usr/env/python3

def main():
    mylist = [1,2,3,4,5, "Python"]
    item = str(mylist[1])
    item2 = str(mylist[5])

    name = input("What is your name?\n> ")

    # This is what you should see when print runs -
    # Hi <name>! Welcome to Day 2 of Python Training!
    print("Hi " + name.capitalize() + "! Welcome to Day " + item + " of " + item2 + " Training!")

main()
