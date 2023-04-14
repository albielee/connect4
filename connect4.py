
class Connect4:
    def __init__(self):
        self.board = [[0]*7]*6
        self.done = False

    def place_chip(pos, player_val):
        place_pos = 0
        for i in range(0, 5):
            square = board[i][pos]
            if(square != 0):
                place_pos = i-1
        if(place_pos != -1)
            board[place_pos][i] = player_val
            return True
        else:
            return False

    def is_move_valid(pos):
        return board[0][pos] == 0

    def check_for_win(x, y, player_val):
        were_good_counter = 0
        
        for d in range(0, 7):
            for i in range(0, 3):
                check_y = y 
                check_x = x

                #west
                if(d == 0):
                    check_x = check_x - i
                #east
                if(d == 1):
                    check_x = check_x + i
                #north
                if(d == 2):
                    check_y = check_y - i
                #south
                if(d == 3):
                    check_y = check_y + i
                #northwest
                if(d == 4):
                    check_y = check_y - i
                    check_x = check_x - i
                #northeast:
                if(d == 5):
                    check_y = check_y - i
                    check_x = check_x + i
                #southeast:
                if(d == 6):
                    check_y = check_y + i
                    check_x = check_x + i
                #southwest
                if(d == 7):
                    check_y = check_y - i
                    check_x = check_x - i
                
                if(check_y >= 0 and check_x >= 0 and check_y <= 5 and check_x <= 6):
                    if(board[check_y][check_x] == player_val):
                        were_good_counter += 1
                    else:
                        break
                else:
                    break
                    
                if(were_good_counter == 4):
                    return True
        
        return False




