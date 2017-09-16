import check_move as c

class bomberman:
    ch = 'B'
    score = 0
    lives_left = 3
    pos = [0,0] #Starting position
    
    def move(self, input_ch, board, bomb_obj):
        next_pos = [0,0]
        next_pos[0] = self.pos[0]
        next_pos[1] = self.pos[1]
        
        if(input_ch == 'w'): #Go up
            next_pos[0] = self.pos[0] - 1

        elif(input_ch == 's'): #Go down
            next_pos[0] = self.pos[0] + 1

        elif(input_ch == 'a'): #Go left
            next_pos[1] = self.pos[1] - 1
                
        elif(input_ch == 'd'): #Go right
            next_pos[1] = self.pos[1] + 1
   
        elif(input_ch == 'b'): #Drop bomb
            x = self.pos[0]
            y = self.pos[1]
            
            bomb_obj.drop_bomb(x,y)

        next_ch = c.check_move(next_pos, board)
        if(next_ch == ' '):
            self.pos[0] = next_pos[0]
            self.pos[1] = next_pos[1]

        elif(next_ch in ('E','^')):
            self.lives_left -= 1
            self.pos[0] = 0
            self.pos[1] = 0
        
        

            
