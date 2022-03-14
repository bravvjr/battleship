import random
import os
from ship import Ship
from board import Board

shots_fired = []

def clear_screen():
    # Clearing the Screen
    # posix is os name for linux or mac
    if(os.name == 'posix'):
        os.system('clear')
        # else screen will be cleared for windows
    else:
        os.system('cls')
    print("WELCOME TO BATTLESHIP\n")

def get_shot(rows, columns):
    shot = []
    target = input("\nInput your target in the format ROW,COLUMN.\n\n")
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

    #Create Battleship
    battleship = Ship("Battleship", 5)

    #Choose difficulty
    while True:
        difficulty = get_difficulty()

        #Create Game Board
        if difficulty == 1:
            player1_board = Board("player1", 5, 5)
            break
        elif difficulty == 2:
            player1_board = Board("player1", 8, 8)
            break
        elif difficulty ==3:
            player1_board = Board("player1", 12, 12)
            valid = True
    
        print("Invalid entry")
        difficulty = get_difficulty()
    
    
    #Place Battleship on game board and then hand coordinates back to the battleship 
    battleship.coordinates = player1_board.place_ship(battleship)
    
    #Print board game
    print(player1_board.print_board())

    while battleship.sunk == False:
        shot = get_shot(player1_board.rows, player1_board.columns)
        if shot == False:
            shot = get_shot(player1_board.rows, player1_board.columns)
        clear_screen()
        hit = player1_board.update_board(shot)
        if hit == "hit":
            if shot in battleship.coordinates:
                battleship.hit()
    finish = input("Game Over! Press Enter to exit game")
    clear_screen()

play_game()