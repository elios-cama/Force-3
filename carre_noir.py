
class CarreNoir():
    
    def __init__(self,x,y):
        
        self.x = x
        self.y = y
        self.pion = None
        
    def deplacerCarre(self, new_x, new_y):
        
        self.x = new_x
        self.y = new_y
        
       