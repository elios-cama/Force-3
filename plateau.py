
from carre_noir import CarreNoir
from Pion import Pion
import numpy as np


#%%

class Plateau():
    
    def __init__(self):
        
        self.plateau = np.empty((3,3), dtype = object)
        
        self.i_vide = 1
        self.j_vide =1 
        
        for i in range(3):
            for j in range(3):
                
                if i == 1 and j==1 :
                    self.plateau[i,j] = None
                    
                else:
                    carre = CarreNoir(i,j)
                    self.plateau[i,j] = carre
                    
    
    
    def afficherPlateau(self):
        
        plateau = np.empty((3,3),dtype=object)
        
        for i in range(3):
            for j in range(3):
                
                if self.plateau[i,j] == None :
                    plateau[i,j] = ''
                
                if self.plateau[i,j] != None and self.plateau[i,j].pion == None :
                    
                    plateau[i,j] = "#"
                
                if self.plateau[i,j] != None and self.plateau[i,j].pion != None :
                    
                    if self.plateau[i,j].pion.couleur == 0 :
                            
                            plateau[i,j] = "R"+str(self.plateau[i,j].pion.numero)
                    
                    if self.plateau[i,j].pion.couleur == 1 :
                            
                            plateau[i,j] = "B"+str(self.plateau[i,j].pion.numero)
   
                            
        print(plateau)
        
    def __getitem__(self, coord):
        i, j = coord
        return self.plateau[i, j]
    
    def __setitem__(self, coord, valeur):
        i, j = coord
        self.plateau[i, j] = valeur