import random

class Bot:

    def __init__(self, value, name="a bot"):
        self.name = name
        self.value = value

    def get_move(self, board):
        pos = random.randint(0,6)
        
        while(not self.is_move_valid(pos, board)):
            pos = random.randint(0,6)
        
        return pos

    def is_move_valid(self, pos, board):
            return board[0][pos] == 0
