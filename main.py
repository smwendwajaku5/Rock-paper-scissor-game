import random
choice = ["rock", "paper", "scissors"]



for i in range (1,10):


    player = input("choice: Rock, Paper, Scissors:").lower()
    computer = random.choice(choice)

    if player == computer:
        print(f"It's a tie Both chose{player}.")

    elif (player == "rock" and computer == "scissors") or \
        (player == "paper" and computer == "rock") or \
        (player == "scissors" and computer == " paper"):

        print(f"you win!!!{player} beats {computer}.")
    else: 
        print(f"computer Wins !!! {computer} beats {player}.")