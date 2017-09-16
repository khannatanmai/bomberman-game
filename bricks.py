import level1 as l

class brick:
    ch = '%'
    pos = l.bricks_at

    def destroy(self, pos_brick): #Remove the specific brick
        if(pos_brick in self.pos):
            self.pos.remove(pos_brick)
            return 1
        
        else:
            return 0
    

        
        
