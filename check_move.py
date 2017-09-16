import positions as p

def check_move(pos_check, board):
    true_pos = p.true_pos(pos_check)

    #We will check the first cell out of the 8 cells of positions

    pos_check = true_pos[0]

    x = int(pos_check[0])
    y = int(pos_check[1])

    return board[x][y] #Return what is on the next position
    
    
    
