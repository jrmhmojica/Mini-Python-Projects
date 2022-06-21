#WELCOME MESSAGE
print("Welcome to the MCU Quiz!")

#VERIFYING IF USER WANTS TO PLAY
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

#PROMPT THAT GAME IS STARTING
print("Let's get started!")

#VARIABLE DECLARATION
score = 0 

#QUESTIONS
answer = input("How many infinity stones are there? ")
if answer == "6":
    score += 1
    print("Correct!")
else:
    print("Incorrect.")

answer = input("What rare metal can be found in Wakanda? ")
if answer.lower() == "vibranium":
    score += 1
    print("Correct!")
else:
    print("Incorrect.")
    
answer = input("What type of radiation was Bruce Banner exposed to? ")
if answer.lower() == "gamma":
    score += 1
    print("Correct!")
else:
    print("Incorrect.")
    
answer = input("What were Tony Stark's last words before the final snap? ")
if answer.lower() == "i am ironman":
    score += 1
    print("Correct!")
else:
    print("Incorrect.")
    
answer = input("What's the name of Captain Marvel's pet? ")
if answer.lower() == "goose":
    score += 1
    print("Correct!")
else:
    print("Incorrect.")
    

print("Your score is " + str(score) + "!")
print("You got " + str(score / 5 * 100) + "%.")