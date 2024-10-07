import random

def choice():
    choices = ["rock", "paper", "scissors"]
    while True:
        player_choice = input("Choose btwn (rock, paper or scissors)/ type quit to exit: ").lower()
        computer_choice = random.choice(choices)
        if player_choice == "quit":
                print("You've exited the game....")
                break
        if player_choice in choices:
            if player_choice == "rock":
                if computer_choice == "paper":
                    print(f"Computer WON!, you chose: {player_choice} and computer chose: {computer_choice} ")
                elif computer_choice == "scissors":
                    print(f"You WON!, you chose: {player_choice} and computer chose: {computer_choice} ")
                else:
                    print(f"I'ts a Tie, you chose: {player_choice} and computer chose: {computer_choice} ")

            if player_choice == "paper":
                if computer_choice == "scissors":
                    print(f"Computer WON!, you chose: {player_choice} and computer chose: {computer_choice} ")
                elif computer_choice == "rock":
                    print(f"You WON!, you chose: {player_choice} and computer chose: {computer_choice} ")
                else:
                    print(f"I'ts a Tie, you chose: {player_choice} and computer chose: {computer_choice} ")

            if player_choice == "scissors":
                if computer_choice == "rock":
                    print(f"Computer WON!, you chose: {player_choice} and computer chose: {computer_choice} ")
                elif computer_choice == "paper":
                    print(f"You WON!, you chose: {player_choice} and computer chose: {computer_choice} ")
                else:
                    print(f"I'ts a Tie, you chose: {player_choice} and computer chose: {computer_choice} ")
        else:
            print("Invalid Input, choose between (rock, paper and scissors)")

                
  
choice()      
    

            
            





            
