#!/usr/bin/env python3
"""input() and print() challenge"""

def main():

    # input asking user's name
    userName = input("Please enter your name: ")
    
    # input asking what day of the week it is
    dayWeek = input("What day of the week is it now: ")

    # print Hello, <name>! Happy <day of week>!
    print("Hello, " + userName + "! Happy", dayWeek + "!")

main()
