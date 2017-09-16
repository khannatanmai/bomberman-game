class wall:
    ch = '#' #character used to represent this object
        
    def insert_into(self,board):
        #Outer Walls
        board[0:2][0:76] = self.ch
        board[36:38][0:76] = self.ch

        #Inner Walls
        for i in range(2,36):
            board[i][0:4] = self.ch
            board[i][72:76] = self.ch

            if(i%4 == 0):
                j = 8
                while(j<76):
                    board[i][j:j+4] = self.ch
                    board[i+1][j:j+4] = self.ch
                    j += 8
