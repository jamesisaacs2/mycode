#!/usr/bin/python3
round = 0
answer = " "

while round < 4 and answer != "Brian":
    # increase counter by 1
    round += 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    answer = answer.capitalize()

    # check if correct answer
    if answer == "Brian": 
        print("That's correct!")
    
    # check for super secret word
    elif answer == "Shrubbery":
	    print("You gave the super secret answer!")
    
    # round up to 4
    elif round == 4:
        print("Sorry, the answer was Brian.")

    # if wrong answerg
    else:
        print("Sorry. Try again!")

