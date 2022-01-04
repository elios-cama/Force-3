from Pion import Pion


class Joueur():
    
    def __init__(self, nom, couleur):
        
        self.nom = nom 
        self.couleur = couleur
        self.pions_en_main = []
        
        #pions posés sur le plateau
        
        self.pions_poses = [None, None, None]
        
        #on attribue des variables aux propriétés de la classe Joueur
        for i in range(3):
            
            pion = Pion(i+1,self.couleur)
            self.pions_en_main.append(pion)
            
        self.doubleD = [False,None]
    