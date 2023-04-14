from connect4 import Connect4
from bot import Bot


def print_board(board):
    for i in board:
        print(i)

game = Connect4()
player1 = Bot(1,"Dan")
player2 = Bot(2,"Albie")
turn = True
while not game.done:
    player = player1 if turn else player2

    move = player.get_move(game.board)

    game.place_chip(move, player.value)

    print_board(game.board)
    print("*"*20)
    print("*"*20)
    print("*"*20)
    print("*"*20)
    print("*"*20)

    turn = not turn
