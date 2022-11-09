#!/usr/bin/env python3
"""Exercise:
    Lists, Input, Print, Variables"""

# import random module
import random

def main():

    # word bank list
    wordbank = ["indentation", "spaces"]

    # students list
    tlgstudents = ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory"
            , "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan"
            , "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    # append int 4 to wordbank
    wordbank.append(4)

    # input asking for a number between 0 and 18, save in var num
    num = int(input("Pick a student number, 0 to 18: "))

    # slice student from list and return as student_name
    student_name = tlgstudents[num]

    # print this output
    # <student_name> always uses <4> <spaces> to indent.
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

    # bonus 1 - randomize student name picked
    name = random.choice(tlgstudents)
    print(name)

    # bonus 2 - The list of TLG students for the course is consistently changing. 
    # Class sizes can expand or diminish with each teaching (although the expectation is that classes will grow!). 
    # Set the num variable to account for changing list lengths, without having to manually recode the list range. 
    # Finally, code the input() to allow the user to type a number beginning from 1 (users don't like to think 
    # about zero-indexing). Hint - Check the Python built-in functions.


main()
