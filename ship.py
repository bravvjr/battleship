import random

class Ship:
    #This class will be used to create the various ships in the game of battleship.
    def __init__ (self, name, length):
        self.name = name
        self.length = length
        self.hits = []
        self.sunk = False
        self.coordinates = []
        for i in range(length):
            self.hits.append(False)
        
    def __repr__ (self):
        if self.sunk == True:
            message = "{name} has been sunk.".format(name = self.name)
        else:
            hits = self.hits.count(True)
            message = "{name} is has been hit {hits} times.".format(name = self.name, hits = hits)
        return message
    
    def hit(self):
        if self.sunk == False:
            self.hits.pop(0)
            self.hits.append(True)
        if False not in self.hits:
            self.sunk = True
        print(self)
        return self.sunk