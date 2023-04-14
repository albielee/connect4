
board = [[0]*7]*6

print(board)

def place_chip(pos, playerVal):
    placePos = 0
    for i in range(0, 5):
        square = board[i][pos]
        if(square != 0):
            placePos = i-1
    if(placePos != -1)
        board[placePos][i] = playerVal
        return True
    else:
        return False

def check_for_win(x, y):
    win = True
    check_x = x
    check_y = y
    while(win):
        if(check_y >= 0 and check_x >= 0 and check_y <= 5 and check_x <= 6):
            board[check_y][check_x] = 

