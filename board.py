import random
from tabulate import tabulate

class Board:
    def __init__ (self, name, size):
        self.name = name
        self.rows = size[0]
        self.columns = size[1]
        self.board = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append("")
            self.board.append(row)
            
    def print_board (self, show=False):
        #Create column headers
        header = []
        for i in range(self.columns):
            header.append(i+1)
        #Creater row headers
        rows = []
        for i in range(self.rows):
            rows.append(chr(i+65))
        if show == True:
            table = self.board
        else:
            table = []
            for row in self.board:
                new_row = []
                for item in row:
                    if item != "X" and item != "O":
                        new_row.append("")
                    else:
                        new_row.append(item)
                table.append(new_row)
                
        #Return formatted table
        return (tabulate(table, header, showindex=rows, numalign="center", stralign="center", tablefmt="fancy_grid"))
    
    def place_ship (self, ship):
        orientation = random.choice(["horizontal", "vertical"])
        coordinates = []
        if orientation == "horizontal":
            #Place ship horizontally
            #Check to make sure the starting point will not result in the ship being placed off the map
            while True:
                start = [random.randint(0,self.rows -1), random.randint(0, self.columns-1)]
                while (start[1] + ship.length > self.columns):
                    start[1] -=1
                #Check to make sure the ship will not be placed over top of another ship
                unique = True
                for i in range(ship.length):
                    if self.board[start[0]][start[1]+i] != "":
                        unique = False
                        break
                if unique == True:
                    break
            for i in range(ship.length):
                self.board[start[0]][start[1]+i] = ship.name[0]
                coordinates.append([start[0],start[1]+i])
        else:
            #Place ship vertically
            #Check to make sure the starting point will not result in the ship being placed off the map
            while True:
                start = [random.randint(0,self.rows -1), random.randint(0, self.columns-1)]
                while (start[0] + ship.length > self.rows):
                    start[0] -=1
                #Check to make sure the ship will not be placed over top of another ship
                unique = True
                for i in range(ship.length):
                    if self.board[start[0]+i][start[1]] != "":
                        unique = False
                        break
                if unique == True:
                    break
            for i in range(ship.length):
                self.board[start[0]+i][start[1]] = ship.name[0]
                coordinates.append([start[0]+i,start[1]])
        return coordinates
        
    
    def update_board (self, coordinate):
        if self.board[coordinate[0]][coordinate[1]] == "":
            self.board[coordinate[0]][coordinate[1]] = "O"
            print(self.print_board(False))
            print("\nYou missed\n")
            return "miss"
        else:
            self.board[coordinate[0]][coordinate[1]] = "X"
            print(self.print_board(False))
            print("\nYou hit\n")
            return "hit"
        
        
    
    

