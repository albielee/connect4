from connect4 import Connect4

game = Connect4()
player1 = 0
player2 = 0
turn = True
while not game.done:
    player = player1 if turn else player2

    move = player.get_move(game.board)

    game.make_move(move)

    turn = not turn

dan
