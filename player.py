from ship import Ship
from board import Board
 
class Player():
    def __init__ (self, name):
        self.name = name
        self.shots_fired = []
        self.ships = []
        self.ships_remaining = 0
    def get_name(self):
        self.name = input("\nWhat is your name?\n\n")
    
    def get_ships(self, num_ships, available_ships):
        for i in range(num_ships):
            self.ships.append(Ship(available_ships[i]["name"], available_ships[i]["length"]))
        self.ships_remaining = num_ships
    
    def get_board(self, size):
        self.board = Board(self.name, size)
        
    def place_ships(self):
        for ship in self.ships:
            ship.coordinates = self.board.place_ship(ship)
    