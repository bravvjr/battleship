import random
import os
from player import Player
from ship import Ship
from board import Board

#Stand ships available in the game
available_ships = [
    {"name": "Battleship", "length": 5},
    {"name": "Cruiser", "length": 4},
    {"name": "Destroyer", "length": 3},
    {"name": "Sub", "length": 2}
    ]

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
def get_shot(player, rows, columns):
    shot = []
    target = input("\nInput your target in the format ROW,COLUMN. For example:\n\nA,1\n\nTarget: ")
    try:
        target = target.split(",")
        for coordinate in target:
            try:
                #Checks for integer
                shot.append(int(coordinate)-1)
            except:
                #Converts letter to integer
                shot.append(ord(coordinate)-65)
        
        #If the input is outside the range of the board
        if shot[0] >= rows or shot[1] >= columns:
            print("You need to enter coordinates that are on the board. Try again.")
            return False
        #If this target has already been tried
        if shot in player.shots_fired:
            print("You have already tried that coordinate. Try again!")
            return False
        #If the shot is valid and not a repeat, it returns
        else:
            player.shots_fired.append(shot)   
            return shot
    except:
        print("Please enter a valid coordinate.")
        return False

def get_players():
    #Get 1 or 2 player game
    players = []
    while True:
        num_players = input("You can play Battleship as a 1 player or 2 player game.\n\n1. 1 Player\n2. 2 Players\n\n")
        if num_players == "1":
            clear_screen()
            name = input("\nWhat is your name?\n\n")
            players.append(Player(name))
            break
        elif num_players == "2":
            clear_screen()
            name = input("\nWhat the name for player 1?\n\n")
            players.append(Player(name))
            clear_screen()
            name = input("\nWhat the name for player 2?\n\n")
            players.append(Player(name))
            break
        else:
            clear_screen()
            print("Please enter a valid option, 1 or 2")
    return players
    
    
def get_difficulty():
    #Choose difficulty
    difficulty = int(input("""Please choose difficulty:\n\n
        1. Easy
        2. Medium
        3. Hard\n\n"""))
    clear_screen()
    return difficulty

def one_player_game():
    clear_screen()
    turn = 0
    while players[0].ships_remaining > 0:
        
        print("\n{player}'s Board".format(player = "Computer"))
        print(players[0].board.print_board(False))
    
        while True:
            shot = get_shot(players[0],players[0].board.rows, players[0].board.columns)
            if shot != False:
                break
        clear_screen()
        print("\n{player}'s Board\n".format(player = "Computer"))        
        hit = players[0].board.update_board(shot)
        if hit == "hit":
            for ship in players[0].ships:
                if shot in ship.coordinates:
                    ship.hit()
                    if ship.sunk == True:
                        players[0].ships_remaining -= 1
        turn += 1
        clear_screen()
    finish = input("Game Over! It took you {turns} turns to win. Press Enter to exit game".format(turns = turn))
    clear_screen()

def two_player_game():
    clear_screen()
    turn = 0
    attacker = 0
    defender = 0
    while players[defender].ships_remaining > 0:
        attacker = turn % 2
        if attacker == 0:
            defender = 1
        else:
            defender = 0
        
        print("Player {player}'s turn".format(player = players[attacker].name))
        print("\n{player}'s Board".format(player = players[attacker].name))
        print(players[attacker].board.print_board(True))

        print("\n{player}'s Board".format(player = players[defender].name))
        print(players[defender].board.print_board(False))
    
        while True:
            shot = get_shot(players[attacker],players[defender].board.rows, players[defender].board.columns)
            if shot != False:
                break
        clear_screen()
        print("Player {player}'s turn".format(player = players[attacker].name))
        print("\n{player}'s Board".format(player = players[attacker].name))
        print(players[attacker].board.print_board(True))

        print("\n{player}'s Board\n".format(player = players[defender].name))        
        hit = players[defender].board.update_board(shot)
        if hit == "hit":
            for ship in players[defender].ships:
                if shot in ship.coordinates:
                    ship.hit()
                    if ship.sunk == True:
                        players[defender].ships_remaining -= 1
        input("\nHit Enter then pass the computer to your partner")
        clear_screen()
        input("Hit Enter when you're ready")
        clear_screen()
        turn += 1
    finish = input("Game Over! Press Enter to exit game")
    clear_screen()

#Initiate the Game
clear_screen()
#Get number of players
players = get_players()
    

#Choose difficulty
while True:
    difficulty = get_difficulty()
    if difficulty == 1 or difficulty == 2 or difficulty ==3:
        break
    print("Invalid input\n")
    

for player in players:
    #Create Game Board
    if difficulty == 1:
        player.get_board(difficulties["easy"][0:2])
        player.get_ships(difficulties["easy"][2], available_ships)
    elif difficulty == 2:
        player.get_board(difficulties["medium"][0:2])
        player.get_ships(difficulties["medium"][2],available_ships)
    elif difficulty == 3:
        player.get_board(difficulties["hard"][0:2])
        player.get_ships(difficulties["hard"][2], available_ships)    
    

#Give each player their ships
for player in players:
    player.place_ships()
    

if len(players) == 1:
    one_player_game()
else:
    two_player_game()