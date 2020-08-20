import random
import sys

#TASK:
#Make a rock-paper-scissors game where it is the player vs the computer. 
#The computer’s answer will be randomly generated, while the program will ask the user for their input. 
#This project will better your understanding of while loops and if statements.

#Solution
generate_choice = random.randint(0,4)


if generate_choice == 0:
    
    computer_hand = "Rock"

elif generate_choice == 1:
    
    computer_hand = "Paper"

elif generate_choice == 2:
    
    computer_hand = "Scissors"

elif generate_choice == 3:
    
    computer_hand = "Lizard"
   
elif generate_choice == 4:
    
    computer_hand = "Spock"


print("Let's play Sheldon's favorite game: Rock-Paper-Scissors-Lizard-Spock")
print("")
print("Please make your choice:")
print("")
print("Rock - press 1")
print("Paper - press 2")
print("Scissors - press 3")
print("Lizard - press 4")
print("Spock - press 5")
print("")

User_choice = input("Your choice: ")
User_choice = int(User_choice)

print("")

if User_choice == 1:
    
    user_hand = "Rock"

elif User_choice == 2:
    
    user_hand = "Paper"

elif User_choice == 3:
    
    user_hand = "Scissors"

elif User_choice == 4:
    
    user_hand = "Lizard"
   
elif User_choice == 5:
    
    user_hand = "Spock"


#Evaluate result

#print(user_hand)
#print(computer_hand)

if computer_hand == "Rock":
    if user_hand == "Rock":
        print("Rock vs Rock = it's a draw!")
    elif user_hand == "Paper":
        print("Your paper covers computer's rock....you win!")
    elif user_hand == "Scissors":
        print("Your scissors got crushed by computer's rock....you lose :-(")
    elif user_hand == "Lizard":
        print("Your lizard got crushed by computer's rock....you lose :-(")
    elif user_hand == "Spock":
        print("Your Spock vaporizes computer's rock....you win!")

if computer_hand == "Paper":
    if user_hand == "Rock":
        print("Your rock is covered by computer's paper....you lose :-(")
    elif user_hand == "Paper":
        print("Paper vs Paper = it's a draw!")
    elif user_hand == "Scissors":
        print("Your scissors cut computer's paper....you win!")
    elif user_hand == "Lizard":
        print("Your lizard eats computer's paper....you win!")
    elif user_hand == "Spock":
        print("Your Spock is disproved by computer's paper....you lose :-(")

if computer_hand == "Scissors":
    if user_hand == "Rock":
        print("Your rock crushes computer's scissors....you win!")
    elif user_hand == "Paper":
        print("Your paper is cut by computer's scissors....you lose :-(")
    elif user_hand == "Scissors":
        print("Scissors vs Scissors = it's a draw!")
    elif user_hand == "Lizard":
        print("Your lizard is decapitated by computer's scissors....you lose :-(")
    elif user_hand == "Spock":
        print("Your Spock smashes computer's scissors....you win!")

if computer_hand == "Lizard":
    if user_hand == "Rock":
        print("Your rock crushes computer's Lizard....you win!")
    elif user_hand == "Paper":
        print("Your paper is eaten by computer's lizard....you lose :-(")
    elif user_hand == "Scissors":
        print("Your scissors decapitated computer's lizard...you win!")
    elif user_hand == "Lizard":
        print("Lizard vs Lizard = it's a draw!")
    elif user_hand == "Spock":
        print("Your Spock is poisoned by computer's lizard....you lose :-(")

if computer_hand == "Spock":
    if user_hand == "Rock":
        print("Your rock is vaporized by computer's Spock...you lose :-(")
    elif user_hand == "Paper":
        print("Your paper disproves computer's Spock....you win :-(")
    elif user_hand == "Scissors":
        print("Your scissors are smashed by computer's Spock...you lose :-(")
    elif user_hand == "Lizard":
        print("Your lizard poisons computer's Spock....you win!")
    elif user_hand == "Spock":
        print("Spock vs Spock = it's a draw!")

print("")
print("Thank you for playing, good luck next time!")
print("")