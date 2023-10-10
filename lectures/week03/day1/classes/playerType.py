from .player import *

class PlayerType(Player):
    def __init__(self, name):
        super().__init__(name)
        self.side = ''

    def addSide(self, side):
        self.side = side
        return self