#!/usr/bin/env python3
count = 0
while True:
    count = count + 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    guess = input("Your guess is? --> ")
    if guess == 'Brian':
        print("That's right, great job!")
        break
    elif count == 4:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry partner, that's not it! Try again!")


