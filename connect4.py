from functools import partial

class Connect4:
    def __init__(self):
        self.board = [[0]*7]*6
        self.done = False

    def place_chip(self, pos, player_val):
        place_pos = 0
        for i in range(0, 5):
            square = self.board[i][pos]
            if (square != 0):
                place_pos = i-1
        if (place_pos != -1):
            self.board[place_pos][i] = player_val
            self.done = self.check_for_win() != -1
            
            return True
        else:
            return False

   
    def check_for_win(self):
        east = [(0,0),(0,1),(0,2),(0,3)]
        south = [(0,0),(1,0),(2,0),(3,0)]
        southeast = [(0,0),(1,1),(2,2),(3,3)]
        southwest = [(0,0),(1,-1),(2,-2),(3,-3)]

        a = lambda x, y: self.board[x[0]+y[0]][x[1]+y[1]]

        for x in range(0, 6):
            for y in range(0, 3):
                pos = (x, y)
                get = partial(a, y=pos)

                if(get(east[0]) == 0):  
                    continue

                if get(east[0]) == get(east[1]) and get(east[1]) == get(east[2]) and get(east[2]) == get(east[3]):
                    return get(east[0])
        
        for x in range(0, 3):
            for y in range(0, 6):
                pos = (x, y)
                get = partial(a, y=pos)

                if(get(south[0]) == 0):  
                    continue

                if get(south[0]) == get(south[1]) and get(south[1]) == get(south[2]) and get(south[2]) == get(south[3]):
                    return get(south[0])
        

        for x in range(0, 3):
            for y in range(0, 4):
                pos = (x, y)
                get = partial(a, y=pos)

                if(get(southeast[0]) == 0):  
                    continue

                if get(southeast[0]) == get(southeast[1]) and get(southeast[1]) == get(southeast[2]) and get(southeast[2]) == get(southeast[3]):
                    return get(southeast[0])

        for x in range(0, 3):
            for y in range(3, 7):
                pos = (x, y)
                get = partial(a, y=pos)

                if(get(southwest[0]) == 0):  
                    continue

                if get(southwest[0]) == get(southwest[1]) and get(southwest[1]) == get(southwest[2]) and get(southwest[2]) == get(southwest[3]):
                    return get(southwest[0])

        return -1