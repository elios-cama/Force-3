
class Pion():
    
    def __init__(self, numero, couleur):
        
        self.numero = numero
        self.couleur = couleur
        
        self.x = None
        self.y = None
        
        
    def deplacerPion(self, new_x, new_y):
        self.x = new_x
        self.y = new_y