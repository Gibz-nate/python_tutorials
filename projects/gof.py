import random


def gof():
    opt = ["WT", "DW"]
    player_pts = 0
    computer_pts = 0
    while True:
        player = input("Choose to work together(WT) or not to work together(DW) to earn points(type QUIT to exit):").upper()
        computer = random.choice(opt)
        if player == "QUIT":
            print("You've exited the game, Have a nice day😊")
            break
        if player in opt:
            if player == "WT":
                if computer == "DW":
                    computer_pts += 5
                    print(f"YOU CHOSE: {player} & COMPUTER CHOSE: {computer}")
                    print(f"computer gained 5 points for not working together \n ================= current points ================== \n computer: {computer_pts}, player: {player_pts}")
            if player == "DW":
                if computer == "WT":
                    player_pts += 5
                    print(f"YOU CHOSE: {player} & COMPUTER CHOSE: {computer}")
                    print(f"You gained 5 points for not working together \n ================= current points ================== \n computer: {computer_pts}, player: {player_pts}")
            if computer == "WT":
                if player == "WT":
                    computer_pts += 3
                    player_pts += 3
                    print(f"YOU CHOSE: {player} & COMPUTER CHOSE: {computer}")
                    print(f"You both gained 3 points for working together \n ================= current points ================== \n computer: {computer_pts}, player: {player_pts}")
            if player == "DW":
                if computer == "DW":
                    print(f"YOU CHOSE: {player} & COMPUTER CHOSE: {computer}")
                    print(f"you both gained 0 points for working together \n ================= current points ================== \n computer: {computer_pts}, player: {player_pts}")          
        else:
            print(f"YOU CHOSE: {player} & COMPUTER CHOSE: {computer}")
            print("Invalid options(choose between WT and DW!!")

gof()
                  

                


            

    

