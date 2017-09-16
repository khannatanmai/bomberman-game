import check_move as c
from random import randint

class enemy:
    ch = 'E'
    alive = 1
    pos = [16,16]

    def move(self, board):
        next_move = randint(0,3) #Next move is random
        next_pos = [0,0]
        next_pos[0] = self.pos[0]
        next_pos[1] = self.pos[1]
        
        if(next_move == 0):
            next_pos[0] = self.pos[0] - 1
                       
        elif(next_move == 1):
            next_pos[0] = self.pos[0] + 1
             
        elif(next_move == 2):
            next_pos[1] = self.pos[1] - 1
            
        elif(next_move == 3):
            next_pos[1] = self.pos[1] + 1

        next_ch = c.check_move(next_pos, board)
        if(next_ch == ' '):
            self.pos[0] = next_pos[0]
            self.pos[1] = next_pos[1]

        elif(next_ch == '^'):
            self.alive = 0
            
