#Rock, paper and scissors game in Python
from random import randint
choices = ["rock", "paper", "scissors"]
playGame = True

while playGame == True:
    computer = choices[randint(0,2)]
    player = input("Choose rock, paper, or scissors?: ").lower()
    
    if computer == player:
        print("Tie!")
        
    elif player == "rock":
        if computer == "scissors":
            print("You win! Rock smashes scissors.")
        else:
            print("You lose. Paper covers rock.")

    elif player == "paper":
        if computer == "rock":
            print("You win! Paper covers rock.")
        else:
            print("You lose. Scissors cut paper.")

    elif player == "scissors":
        if computer == "paper":
            print("You win! Scissors cut paper.")
        else:
            print("You lose. Rock smashes scissors.")
    
    else:
        print("Not a valid play. Check your spelling and try again.")
        continue
        
    keepPlaying = input("Play again? ").lower()

    if keepPlaying == "no":
        playGame = False
        print("Thanks for playing!")
    elif keepPlaying == "yes":
        playGame = True
    else:
        print("Not a valid play. Please type 'yes' or 'no'.")
    
