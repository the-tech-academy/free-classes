from random import randint

choices = ["Rock", "Paper", "Scissors"]

playGame = True

while playGame == True:
    
    computer = choices[randint(0,2)].lower()
    player = input("Rock, Paper, or Scissors?: ").lower()
    
    if computer == player:
        print("Tie!")
        
    elif player == "rock":
        
        if computer == "paper":
            print("You lose", computer, "covers", player)

        else:
            print("You win!", player, "smashes", computer)

    elif player == "paper":

        if computer == "scissors":
            print("You lose", computer, "cuts", player)

        else:
            print("You win!", player, "covers", computer)

    elif player == "scissors":

        if computer == "rock":
            print("You lose", computer, "smashes", player)

        else:
            print("You win!", player, "cuts", computer)

    
    else:
        print("That's not a valid play. Check your spelling and try again.")
        
    keepPlaying = input("Would you like to play again? yes/no: ").lower()

    if keepPlaying == "no":
        playGame = False
        print("Thanks for playing!")
    
