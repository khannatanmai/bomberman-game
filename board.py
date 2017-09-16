import numpy as np
import wall as w
import positions as p
import check_move as cm

class board: #Board size is 38*76
    layout = np.zeros((38,76),dtype=str)

    def update(self, bman_obj, enemy_obj, brick_obj, bomb_obj):
        #initializing all to empty strings
        self.layout[0:38][0:76] = ' '

        #insert walls
        
        wall_obj = w.wall()
        wall_obj.insert_into(self.layout)

        #insert bomberman if alive
        
        if(bman_obj.lives_left >= 0):
            pos_tofill = p.true_pos(bman_obj.pos)
            #Fill 8 bytes with the bomberman
            for i in range(8):
                x = int(pos_tofill[i][0])
                y = int(pos_tofill[i][1])
            
                self.layout[x][y] = bman_obj.ch

        #insert enemy if alive
        
        if(enemy_obj.alive == 1):
            pos_tofill = p.true_pos(enemy_obj.pos)
            #Fill 8 bytes with the enemy
            for i in range(8):
                x = int(pos_tofill[i][0])
                y = int(pos_tofill[i][1])
            
                self.layout[x][y] = enemy_obj.ch

        #insert bricks

        all_bricks = brick_obj.pos #Array with positions of all bricks

        for j in all_bricks:
            pos_tofill = p.true_pos(j)
            #Fill 8 bytes with one brick
            for i in range(8):
                x = int(pos_tofill[i][0])
                y = int(pos_tofill[i][1])
            
                self.layout[x][y] = brick_obj.ch
        
        #insert bombs

        all_bombs = bomb_obj.pos_and_timer #Array with positions of all bombs
        for j in all_bombs:

            xc = j[0]
            yc = j[1]
            
            pos_tofill = p.true_pos([xc,yc])
            #Fill 8 bytes with one bomb
            for i in (0,4):
                x = int(pos_tofill[i][0])
                y = int(pos_tofill[i][1])
                self.layout[x][y] = '['

            for i in (3,7):
                x = int(pos_tofill[i][0])
                y = int(pos_tofill[i][1])
            
                self.layout[x][y] = ']'

            for i in (1,2,5,6):
                x = int(pos_tofill[i][0])
                y = int(pos_tofill[i][1])
            
                self.layout[x][y] = int(j[2]/3) #timer of this bomb

        #insert explosion
        pos_expl = bomb_obj.current_explosion

        if pos_expl:
            pos = [0,0]
            pos[0] = pos_expl[0][0]
            pos[1] = pos_expl[0][1]
            
            pos_tocheck = [0,0]

            #PUT EXPLOSION AT BOMB CURRENT POSITION
            pos_tocheck[0] = pos[0]
            pos_tocheck[1] = pos[1]
            
            pos_tofill = p.true_pos(pos_tocheck)

            #Fill 8 bytes with one explosion
            for i in range(8):
                x = int(pos_tofill[i][0])
                y = int(pos_tofill[i][1])
                        
                self.layout[x][y] = '^'

            #CHECKING IF EXPLOSION CAN GO RIGHT
            pos_tocheck[0] = pos[0]
            pos_tocheck[1] = pos[1]
            
            for j in range(1,3): 
                pos_tocheck[0] = pos[0] + j
                if(cm.check_move(pos_tocheck, self.layout) == '#'):
                    break
                else:
                    pos_tofill = p.true_pos(pos_tocheck)

                    #Fill 8 bytes with one explosion
                    for i in range(8):
                        x = int(pos_tofill[i][0])
                        y = int(pos_tofill[i][1])
                        
                        self.layout[x][y] = '^'

                    #Destroy bricks at this spot if any
                    if(brick_obj.destroy(pos_tocheck) == 1):
                        bman_obj.score += 20
                    #returns 1 if a brick was destroyed

            #CHECKING IF EXPLOSION CAN GO LEFT
            pos_tocheck[0] = pos[0]
            pos_tocheck[1] = pos[1]
            
            for j in range(1,3):
                pos_tocheck[0] = pos[0] - j
                if(cm.check_move(pos_tocheck, self.layout) == '#'):
                    break
                else:
                    pos_tofill = p.true_pos(pos_tocheck)

                    #Fill 8 bytes with one explosion
                    for i in range(8):
                        x = int(pos_tofill[i][0])
                        y = int(pos_tofill[i][1])
                        
                        self.layout[x][y] = '^'

                    #Destroy bricks at this spot if any
                    if(brick_obj.destroy(pos_tocheck) == 1):
                        bman_obj.score += 20
                    #returns 1 if a brick was destroyed 


            #CHECKING IF AN EXPLOSION CAN GO UP
            pos_tocheck[0] = pos[0]
            pos_tocheck[1] = pos[1]
            
            for j in range(1,3):
                pos_tocheck[1] = pos[1] + j
                if(cm.check_move(pos_tocheck, self.layout) == '#'):
                    break
                else:
                    pos_tofill = p.true_pos(pos_tocheck)

                    #Fill 8 bytes with one explosion
                    for i in range(8):
                        x = int(pos_tofill[i][0])
                        y = int(pos_tofill[i][1])
                        
                        self.layout[x][y] = '^'

                    #Destroy bricks at this spot if any
                    if(brick_obj.destroy(pos_tocheck) == 1):
                        bman_obj.score += 20
                    #returns 1 if a brick was destroyed

            #CHECKING IF AN EXPLOSION CAN GO DOWN
            pos_tocheck[0] = pos[0]
            pos_tocheck[1] = pos[1]
            
            for j in range(1,3):
                pos_tocheck[1] = pos[1] - j
                if(cm.check_move(pos_tocheck, self.layout) == '#'):
                    break
                else:
                    pos_tofill = p.true_pos(pos_tocheck)

                    #Fill 8 bytes with one explosion
                    for i in range(8):
                        x = int(pos_tofill[i][0])
                        y = int(pos_tofill[i][1])
                        
                        self.layout[x][y] = '^'
            
                    #Destroy bricks at this spot if any
                    if(brick_obj.destroy(pos_tocheck) == 1):
                        bman_obj.score += 20
                    #returns 1 if a brick was destroyed
