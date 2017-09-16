import time

class bomb:
    pos_and_timer = [] #[[pos_x,pos_y,time_left],[..],...]
    current_explosion = [] #[[pos_x, pos_y, time_left]]
    explode_time = 12
    explosion_stay = 2

    def drop_bomb(self, pos_x, pos_y):
        self.pos_and_timer.append([pos_x,pos_y,self.explode_time])

    def explode(self, element):
        self.current_explosion.append([element[0],element[1],
                                       self.explosion_stay])
        self.pos_and_timer.remove(element)

    def remove_explosion(self): 
        self.current_explosion.clear()

    def countdown(self):
        for i in self.current_explosion:
            self.current_explosion[0][2] -= 1 #decrement time

            if(i[2] < 0): #If 0 sec left, remove explosion
                self.remove_explosion()

        for i in self.pos_and_timer:
            index = self.pos_and_timer.index(i)
            self.pos_and_timer[index][2] -= 1 #decrement time

            if(i[2] < 0): #If 0 sec left, explode
                self.explode(i)

                
    
                
