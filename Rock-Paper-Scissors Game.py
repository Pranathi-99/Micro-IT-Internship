import random
#random module has been imported to generate random number i.e Rock, Paper or Scissors

def RPS_game():
    #function initialization and definition
    player_score = 0
    machine_score = 0
    #initially scores are zero
    
    rounds=int(input("Enter the Number of Rounds you want to play: "))
    for i in range(rounds):
        #input user's choice
        player_choice = input("Enter a choice to start playing(rock, paper, scissors): ").lower()

        #validate the user's choice
        while player_choice not in ["rock", "paper", "scissors"]:
            player_choice = input("Invalid input. Enter rock, paper, or scissors: ").lower()

        #Computer's choice
        choices = ["rock", "paper", "scissors"]
        machine_choice = random.choice(choices)
        print(f"\nYou chose {player_choice}, Machine chose {machine_choice}.\n")

        #Declare the winner
        if player_choice == machine_choice:
            print(f"Both chose {player_choice}. It's a tie!")
        
        elif player_choice == "paper":
            if machine_choice == "rock":
                print("Paper covers rock! You win this round!")
                player_score += 1
            else:
                print("Scissors cuts paper! You lose this round.")
                machine_score += 1

        elif player_choice == "rock":
            if machine_choice == "scissors":
                print("Rock smashes scissors! You win this round!")
                player_score += 1
            else:
                print("Paper covers rock! You lose this round.")
                machine_score += 1
                
        elif player_choice == "scissors":
            if machine_choice == "paper":
                print("Scissors cuts paper! You win this round!")
                player_score += 1
            else:
                print("Rock smashes scissors! You lose this round.")
                machine_score += 1

        #current score print
        print(f"\nScore - You: {player_score}, Machine: {machine_score}\n")

    #final score print
    print(f"\nFinal Score - You: {player_score}, Machine: {machine_score}")

    #final result print
    if player_score > machine_score:
        print("Congratulations! You are the Winner!")
    elif player_score < machine_score:
        print("You lose the game. Better luck next time!")
    else:
        print("Game is tie!")
    #Conditional statements are used to control the program flow
        
#main program
if __name__ == "__main__":
    print("Welcome to the game")
    print("\n *-*-*-*-*-*-*  Rock-Paper-Scissors  *-*-*-*-*-*-* \n")
    RPS_game()
    #function call
    
    play_again = input("\nPlay again? (yes/no): ").lower()
    while play_again not in ["yes", "no"]:
        play_again = input("Invalid input. Please enter yes or no: ").lower()
    if play_again == "yes":
        RPS_game()
    else:
        print("Thank you")

"""
Sample Output:
Welcome to the game

 *-*-*-*-*-*-*  Rock-Paper-Scissors  *-*-*-*-*-*-* 

Enter the Number of Rounds you want to play: 2
Enter a choice to start playing(rock, paper, scissors): PAPER

You chose paper, Machine chose paper.

Both chose paper. It's a tie!

Score - You: 0, Machine: 0

Enter a choice to start playing(rock, paper, scissors): Rock

You chose rock, Machine chose scissors.

Rock smashes scissors! You win this round!

Score - You: 1, Machine: 0


Final Score - You: 1, Machine: 0
Congratulations! You are the Winner!

Play again? (yes/no): no
Thank you
"""

        
