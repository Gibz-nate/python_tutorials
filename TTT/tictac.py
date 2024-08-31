import random

def choose():
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        player = input("Choose between rock, paper, and scissors: ").lower()
        if player in choices:
            break
        else:
            print("Invalid choice. Please choose again.")

    computer = random.choice(choices)

    if player == computer:
        print("It's a draw!")    
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        print(f"You WIN!\n{player.capitalize()} beats {computer}.")
    else:
        print(f"You LOST!\n{computer.capitalize()} beats {player}.")

choose()




    
