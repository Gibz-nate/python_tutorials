import random

def gof():
    opt = ["WT", "DW"]
    player_pts = 0
    computer_pts = 0
    rounds = 10  # Set the number of rounds
    computer_behavior = []  # Track player behavior

    print(f"Welcome to the Game of Life! You have {rounds} rounds to play.")
    print("Choose to work together (WT) or not to work together (DW) to earn points.")

    for round in range(1, rounds + 1):
        print(f"\n======= Round {round} =======")
        player = input("Your choice (WT or DW, or type 'quit' to exit): ").upper()

        if player == "QUIT":
            print("You've exited the game. Have a nice day😊")
            break

        # Computer decision with adaptive strategy
        if len(computer_behavior) >= 2 and computer_behavior[-1] == "DW" and computer_behavior[-2] == "DW":
            computer = "DW"  # If the player betrayed twice, the computer will choose DW
        else:
            computer = random.choice(opt)  # Otherwise, random choice
        
        computer_behavior.append(player)  # Store player behavior
        
        if player not in opt:
            print("Invalid choice. Please choose between WT and DW!")
            continue

        # Symmetrical payoffs for choices
        if player == "WT" and computer == "WT":
            player_pts += 3
            computer_pts += 3
            print(f"YOU CHOSE: {player} & COMPUTER CHOSE: {computer}")
            print(f"You both gained 3 points for working together.")
        
        elif player == "DW" and computer == "DW":
            print(f"YOU CHOSE: {player} & COMPUTER CHOSE: {computer}")
            print(f"You both gained 0 points for not working together.")
        
        elif player == "WT" and computer == "DW":
            computer_pts += 5
            print(f"YOU CHOSE: {player} & COMPUTER CHOSE: {computer}")
            print(f"Computer gained 5 points for not working together.")
        
        elif player == "DW" and computer == "WT":
            player_pts += 5
            print(f"YOU CHOSE: {player} & COMPUTER CHOSE: {computer}")
            print(f"You gained 5 points for not working together.")

        # Display the current points after each round
        print(f"================= Current Points ==================")
        print(f"Computer: {computer_pts}, Player: {player_pts}")
    
    # Game over: determine the winner
    if player != "QUIT":
        print("\n======= Game Over =======")
        if player_pts > computer_pts:
            print(f"Congratulations! You won with {player_pts} points!")
        elif computer_pts > player_pts:
            print(f"Computer wins with {computer_pts} points.")
        else:
            print(f"It's a tie! Both have {player_pts} points.")

gof()
