#IMPORT MODULE
import random

#VARIABLE DECLARATION
top_of_range = 0
guesses = 0

#ASKING USER FOR INPUT AND CHECKING IF IT IS VALID
while top_of_range <= 0:
    
    #asking for the number
    print("Type a number: ")
    top_of_range = input()
    
    #checking if the user entered a number
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        
        #checking if the user entered a positive number
        if top_of_range <= 0:
            print("Please type a number greater than 0")
    else:
        print("Please type a number")
        top_of_range = 0

#GENERATING A RANDOM NUMBER
random_number = random.randrange(top_of_range + 1)

#USER IS GUESSING
while True:
    guesses += 1
    user_guess = input("Guess a number from 0 to " + str(top_of_range) + ": ")

    #CHECKING IF USER ENTERS A NUMBER
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number.")
        continue
    
    #CHECKING IF USER ENTERS A NUMBER WITHIN THE RANGE
    if user_guess > top_of_range:
        print("Please guess a number from 0 to " + str(top_of_range) + ".")

    #USER GUESSES CORRECTLY
    if user_guess == random_number:
        print("You got it! It took you", guesses, "guesses to get the right number.")
        break
    #USER GUESSES WRONG
    elif user_guess < random_number:
        print("Guess higher")
    else: 
        print("Guess lower")
        