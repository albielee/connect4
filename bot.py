class Bot:

    def __init__(self, name="a bot"):
        self.name = name

    def get_move(self, board):
        raise NotImplementedError("bot needs make_move function")
