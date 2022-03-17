import random
import os
from ship import Ship
from board import Board

#Stand ships available in the game
available_ships = [
    {"name": "Battleship", "length": 5},
    {"name": "Cruiser", "length": 4},
    {"name": "Destroyer", "length": 3},
    {"name": "Sub", "length": 2}
    ]

#This stores the commulative shots attempted
shots_fired = []

#This is the settings for difficulty levles in the form for [rows, columns, # of ships]
difficulties = {
    "easy" : [5, 5, 1],
    "medium" : [8, 8, 2],
    "hard" : [10, 10, 4]
}

def clear_screen():
    # Clearing the Screen
    # posix is os name for linux or mac
    if(os.name == 'posix'):
        os.system('clear')
        # else screen will be cleared for windows
    else:
        os.system('cls')
    print("WELCOME TO BATTLESHIP\n")

#This function will get the user inputed target and check it for validity.
def get_shot(rows, columns):
    shot = []
    target = input("\nInput your target in the format ROW,COLUMN. For example:\n\nA,1\n\nTarget: ")
    try:
        target = target.split(",")
        for coordinate in target:
            try:
                shot.append(int(coordinate)-1)
            except:
                shot.append(ord(coordinate)-65)
        if shot[0] >= rows or shot[1] >= columns:
            print("You need to enter coordinates that are on the board. Try again.")
            return False
        if shot in shots_fired:
            print("You have already tried that coordinate. Try again!")
            return False
        else:
            shots_fired.append(shot)   
            return shot
    except:
        print("Please enter a valid coordinate.")
        return False
    
def get_difficulty():
    #Choose difficulty
    difficulty = int(input("""Please choose difficulty:\n\n
        1. Easy
        2. Medium
        3. Hard\n\n"""))
    clear_screen()
    return difficulty

def play_game():
    clear_screen()
    ships = {}
    #Choose difficulty
    while True:
        difficulty = get_difficulty()
        
        #Create Game Board
        if difficulty == 1:
            player1_board = Board("player1", difficulties["easy"][0:2])
            for i in range(difficulties["easy"][2]):
                ships[available_ships[i]["name"]] = Ship(available_ships[i]["name"], available_ships[i]["length"])
            ships["remaining"] = 1
            break
        elif difficulty == 2:
            player1_board = Board("player1", difficulties["medium"][0:2])
            for i in range(difficulties["medium"][2]):
                ships[available_ships[i]["name"]] = Ship(available_ships[i]["name"], available_ships[i]["length"])
            ships["remaining"] = 2
            break
        elif difficulty == 3:
            player1_board = Board("player1", difficulties["hard"][0:2])
            for i in range(difficulties["hard"][2]):
                ships[available_ships[i]["name"]] = Ship(available_ships[i]["name"], available_ships[i]["length"])
            ships["remaining"] = 4
            break
        
        print("Invalid entry")
        #difficulty = get_difficulty()    
    
    #Place ships on game board and then hand coordinates back to the battleship 
    for i in range(len(ships)-1):
        ships[available_ships[i]["name"]].coordinates = player1_board.place_ship(ships[available_ships[i]["name"]])
    
    #Print board game
    print(player1_board.print_board())

    while ships["remaining"] > 0:
        while True:
            shot = get_shot(player1_board.rows, player1_board.columns)
            if shot != False:
                break
        clear_screen()
        hit = player1_board.update_board(shot)
        if hit == "hit":
            for i in range(len(ships)-1):
                if shot in ships[available_ships[i]["name"]].coordinates:
                    ships[available_ships[i]["name"]].hit()
                    if ships[available_ships[i]["name"]].sunk == True:
                        ships["remaining"] -= 1
    finish = input("Game Over! Press Enter to exit game")
    clear_screen()

play_game()