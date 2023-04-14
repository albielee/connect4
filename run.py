from connect4 import Connect4
from bot import Bot


def print_board(board):
    for i in board:
        print(i)


def run_game(printing=False):

    game = Connect4()
    player1 = Bot(1, "Dan")
    player2 = Bot(2, "Albie")
    turn = True
    while (not game.done) and any(a == 0 for a in game.board[0]):
        player = player1 if turn else player2

        move = player.get_move(game.board)
        game.place_chip(move, player.value)

        if printing:
            print_board(game.board)
            print("*"*20)
            print("*"*20)

            input()

        turn = not turn

    if printing:
        print(f"winner is {game.winner}")

    return game.winner


winners = []
for i in range(100):
    winners.append(run_game())

print(f"player1 wins: {sum([a==1 for a in winners])}")
print(f"player2 wins: {sum([a==2 for a in winners])}")
