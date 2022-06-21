#IMPORT MODULE
import random

#VARIABLE DECLARATION
user_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

#USER IS PLAYING
while True:

    #USER CHOOSES
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        break
    if user_input not in options:
        print("Please type a valid answer.")
        continue

    #COMPUTER CHOOSES
    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_choice = options[random_number]
    
    #SHOWING PICKS
    print("Computer picked " + computer_choice)
    print("You picked " + user_input)
    
    #DETERMINING WINNER
    if user_input == "rock" and computer_choice == "scissors":
        print("You won!")
        user_score += 1
    elif user_input == "paper" and computer_choice == "rock":
        print("You won!")
        user_score += 1
    elif user_input == "scissors" and computer_choice == "paper":
        print("You won!")
        user_score += 1
    elif user_input == computer_choice:
        print("It's a draw!")
    else:
        print("You lost!")
        computer_score += 1

#SHOWING RESULTS
if user_score > computer_score:
    print("Congratulations! You beat the computer!")
else: 
    print("You suck! Better luck next time.")

print("Your score:", user_score)
print("Computer's score:", computer_score)

#BYE
print("Goodbye!")