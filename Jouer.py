# -*- coding: utf-8 -*-
"""
Created by Elios Cama, Christian Do, Nathan Damette
2022
"""


class Jouer:
    
    def __init__(self, joueur1, joueur2, plateau):
        
        self.j1 = joueur1
        self.j2 = joueur2
        
        self.plateau =  plateau
        
        
        
    
    def deplacement_carre(self, carre):
        
        i = carre.x
        j = carre.y
        
        carre.deplacerCarre(self.plateau.i_vide, self.plateau.j_vide)
        
        if self.plateau[i,j].pion != None :
            carre.pion.x = carre.x
            carre.pion.y = carre.y
            
        self.plateau[carre.x, carre.y] = carre
        self.plateau[i,j] = None
        self.plateau.i_vide = i
        self.plateau.j_vide = j
        
    def poser_pion(self, joueur, carre):
        
        i_pion = 0
        
        while joueur.pions_en_main[i_pion] == None and i_pion < 3:
            i_pion+=1 
        
        pion = joueur.pions_en_main[i_pion]
        pion.deplacerPion(carre.x, carre.y)
        
        #pose le pion sur le jeu et ajoute dans liste de pions posés
        joueur.pions_poses[i_pion] = pion
        #add pion sur le carré en question
        carre.pion = joueur.pions_poses[i_pion]
        
        #enleve le pion de la main du joueur car il est sur le plateau
        joueur.pions_en_main[i_pion] = None
        
        
            
    def deplacer_pion(self, joueur,carre, pion) :
        
        """
        pion deja sur le plateau donc sur un carre
        """
       
        i_pion = pion.x
        j_pion = pion.y
          
        pion.deplacerPion(carre.x, carre.y)
        carre.pion = pion
        try:
            self.plateau[i_pion,j_pion].pion = None
            
        except AttributeError:
            pass
        
        
        
        
       
        
        
    def deplacer_carre_x2(self, joueur, adversaire, sens = None ):
        
        Deplacement = False
        if adversaire.doubleD[0] == True and adversaire.doubleD[1] != None : 
        
            #coin haut gauche
                
                if (self.plateau.i_vide, self.plateau.j_vide) == (0,0) :
                    
                    if adversaire.doubleD[1] == 'd':
                        self.deplacement_carre(self.plateau[1,0])
                        self.deplacement_carre(self.plateau[2,0])
                        Deplacement = True
                        joueur.doubleD[1] = 'h'
                        
                    elif adversaire.doubleD[1] == 'b':
                        self.deplacement_carre(self.plateau[0,1])
                        self.deplacement_carre(self.plateau[0,2])
                        Deplacement = True
                        joueur.doubleD[1] = 'g'
                #coin haut droit
                
                elif (self.plateau.i_vide, self.plateau.j_vide) == (0,2) :
                    
                    if adversaire.doubleD[1] == 'g':
                        self.deplacement_carre(self.plateau[1,2])
                        self.deplacement_carre(self.plateau[2,2])
                        Deplacement = True
                        joueur.doubleD[1] = 'h'
                    
                    elif adversaire.doubleD[1] == 'b':
                        self.deplacement_carre(self.plateau[0,1])
                        self.deplacement_carre(self.plateau[0,0])
                        Deplacement = True
                        joueur.doubleD[1] = 'd'
                #coin bas gauche
                
                elif (self.plateau.i_vide, self.plateau.j_vide) == (2,0) :
                    
                    if adversaire.doubleD[1] == 'd':
                        self.deplacement_carre(self.plateau[1,0])
                        self.deplacement_carre(self.plateau[0,0])
                        Deplacement = True
                        joueur.doubleD[1] = 'b'
                    
                    elif adversaire.doubleD[1] == 'h':
                        self.deplacement_carre(self.plateau[2,1])
                        self.deplacement_carre(self.plateau[2,2])
                        Deplacement = True
                        joueur.doubleD[1] = 'g'
                        
                #coin bas droit
                
                elif (self.plateau.i_vide, self.plateau.j_vide) == (2,2) :
                    
                    if adversaire.doubleD[1] == 'g':
                        self.deplacement_carre(self.plateau[1,2])
                        self.deplacement_carre(self.plateau[0,2])
                        Deplacement = True
                        joueur.doubleD[1] = 'b'
                        
                    elif adversaire.doubleD[1] == 'h':
                        self.deplacement_carre(self.plateau[2,1])
                        self.deplacement_carre(self.plateau[2,0])
                        Deplacement = True
                        joueur.doubleD[1] = 'd'
        
        if adversaire.doubleD[0] == False :
            
            
            
            if sens == None :
                
                #vide à la position 0,1
                
                if self.plateau.i_vide == 0 and self.plateau.j_vide == 1 :
                    
                    self.deplacement_carre(self.plateau[1,1])
                    self.deplacement_carre(self.plateau[2,1])
                    Deplacement = True
                #vide à la position 1,0
                
                elif (self.plateau.i_vide, self.plateau.j_vide) == (1,0) :
                    
                    self.deplacement_carre(self.plateau[1,1])
                    self.deplacement_carre(self.plateau[1,2])
                    Deplacement = True
                #vide à la position 1,2
                
                elif (self.plateau.i_vide, self.plateau.j_vide) == (1,2) :
                    
                    self.deplacement_carre(self.plateau[1,1])
                    self.deplacement_carre(self.plateau[1,0])
                    Deplacement = True
                #vide à la position 2,1
                
                elif (self.plateau.i_vide, self.plateau.j_vide) == (2,1) :
                    
                    self.deplacement_carre(self.plateau[1,1])
                    self.deplacement_carre(self.plateau[0,1])
                    Deplacement = True
            else :
               
                #coin haut gauche
                
                if (self.plateau.i_vide, self.plateau.j_vide) == (0,0) :
                    
                    if sens == 'h':
                        self.deplacement_carre(self.plateau[1,0])
                        self.deplacement_carre(self.plateau[2,0])
                        Deplacement = True
                        joueur.doubleD[1] = 'h'
                    elif sens == 'g':
                        self.deplacement_carre(self.plateau[0,1])
                        self.deplacement_carre(self.plateau[0,2])
                        Deplacement = True
                        joueur.doubleD[1] = 'g'
                #coin haut droit
                
                elif (self.plateau.i_vide, self.plateau.j_vide) == (0,2) :
                    
                    if sens == 'h':
                        self.deplacement_carre(self.plateau[1,2])
                        self.deplacement_carre(self.plateau[2,2])
                        Deplacement = True
                        joueur.doubleD[1] = 'h'
                    
                    elif sens == 'd':
                        self.deplacement_carre(self.plateau[0,1])
                        self.deplacement_carre(self.plateau[0,0])
                        Deplacement = True
                        joueur.doubleD[1] = 'd'
                #coin bas gauche
                
                elif (self.plateau.i_vide, self.plateau.j_vide) == (2,0) :
                    
                    if sens == 'b':
                        self.deplacement_carre(self.plateau[1,0])
                        self.deplacement_carre(self.plateau[0,0])
                        Deplacement = True
                        joueur.doubleD[1] = 'b'
                    
                    elif sens == 'g':
                        self.deplacement_carre(self.plateau[2,1])
                        self.deplacement_carre(self.plateau[2,2])
                        Deplacement = True
                        joueur.doubleD[1] = 'g'
                        
                #coin bas droit
                
                elif (self.plateau.i_vide, self.plateau.j_vide) == (2,2) :
                    
                    if sens == 'b':
                        self.deplacement_carre(self.plateau[1,2])
                        self.deplacement_carre(self.plateau[0,2])
                        Deplacement = True
                        joueur.doubleD[1] = 'b'
                        
                    elif sens == 'd':
                        self.deplacement_carre(self.plateau[2,1])
                        self.deplacement_carre(self.plateau[2,0])
                        Deplacement = True
                        joueur.doubleD[1] = 'd'
        
        return Deplacement
    
    
    def choix_action_joueur(self, joueur, adversaire):
        
        
        ListeChoix = [1,2,3,4]
        
        if joueur.pions_en_main == [None]*3 :
                ListeChoix[1] = None 
        
        #pas de pions poses
        if joueur.pions_poses == [None]*3 :
            ListeChoix[2] = None
        
        #condition double deplacement
        if (adversaire.doubleD[0] == True and adversaire.doubleD[1] == None)  or (self.plateau.i_vide == 1 and self.plateau.j_vide == 1):
            ListeChoix[3]= None
            
        ListeChoix = [x for x in ListeChoix if x!= None]
        
        dictionnaireChoix ={
            "1" : "Deplacer carré",
            "2" : "Poser un pion",
            "3" : "Deplacer un pion",
            "4" : "Double deplacement"           
            }
        
        print("Joueur {}  : Faites un choix d'action \n".format(joueur.nom))
        
        for x in ListeChoix :
            print("{} : {}".format(str(x),dictionnaireChoix[str(x)]))
        
        choix = int(input("Choix  :  "))
        
        while choix not in ListeChoix :
            choix = int(input("Choix non valide, nouveau choix  : \n "))
        
        
        if choix == 1 :
            
            i_vide = self.plateau.i_vide +1
            j_vide = self.plateau.j_vide +1
            
            import numpy as np
            
            ListeDeplacement = []
            TabTest = np.pad(self.plateau.plateau,1)
            
            for k in range(i_vide-1, i_vide+2):
                for l in range(j_vide-1, j_vide+2):
                   
                    
                        
                     if (k == i_vide and (l == (j_vide-1) or l == (j_vide+1))) :
                          
                          if TabTest[k,l] != 0 : 
                              
                              ListeDeplacement.append((k-1,l-1))
                          
                              
                           
                     if (l == j_vide and (k ==(i_vide-1) or k == (i_vide+1))) :
                         
                         if TabTest[k,l] != 0 :
                            
                            ListeDeplacement.append((k-1,l-1))
                        
            print("Déplacements autorisés : \n ") 
            for i in range(len(ListeDeplacement)) :
                print("Choix {} : = {}".format(i+1,ListeDeplacement[i]))
            print("\n")
            
            numDeplacement = int(input("Numéro du choix de déplacement : "))
           
            while numDeplacement > len(ListeDeplacement) :
                numDeplacement = int(input("Numéro non valide, nouveau choix  : "))
            
            choixDeplacement = ListeDeplacement[numDeplacement-1]
            
            self.deplacement_carre(self.plateau[choixDeplacement[0],choixDeplacement[1]])
            joueur.doubleD = [False, None]
        
        elif choix == 2 :
            
            ListeCase = []
            for i in range(3) :
                for j in range(3):
                    
                    if self.plateau[i,j] != None and self.plateau[i,j].pion == None :
                        ListeCase.append((i,j))
       
            
            print("Cases autorisées : \n ") 
            
            for i in range(len(ListeCase)) :
                print("Choix {} : = {}".format(i+1,ListeCase[i]))
            print("\n")
            
            numCase = int(input("Numéro du choix de case : "))
           
            while numCase > len(ListeCase) :
                numCase = int(input("Numéro non valide, nouveau choix  : "))
            
            
            choixCase = ListeCase[numCase-1]
            self.poser_pion(joueur,self.plateau[choixCase[0],choixCase[1]])
            joueur.doubleD = [False,None]
            
     
        elif choix == 3 :
            
            #1 seul pion poses (alors c'est le premier)
            if len([pion for pion in joueur.pions_poses if pion != None]) == 1:
                pion = joueur.pions_poses[0]
            
            else :
                
                numPion = int(input("Numéro du pion que vous voulez deplacer : "))
                
                if 3 < numPion or numPion<0 :
                    while 3 < numPion or numPion<0 :
                        numPion = int(input("Vous n'avez que trois pions : "))

                while joueur.pions_poses[numPion-1] == None : 
                    
                    numPion = int(input("Ce pion est dans votre main donner un autre pion  : "))
                    if 3 < numPion or numPion<0 :
                        while 3 < numPion or numPion<0 :
                            numPion = int(input("Vous n'avez que trois pions : "))
                
                pion = joueur.pions_poses[numPion-1]
            
            ListeCase = []
            for i in range(3) :
                for j in range(3):
                    
                    if self.plateau[i,j] != None and self.plateau[i,j].pion == None :
                        ListeCase.append((i,j))
       
            
            print("Cases autorisées : \n ") 
            
            for i in range(len(ListeCase)) :
                print("Choix {} : = {}".format(i+1,ListeCase[i]))
            print("\n")
            
            numCase = int(input("Numéro du choix de case : "))
           
            while numCase > len(ListeCase) :
                numCase = int(input("Numéro non valide, nouveau choix  : "))
            
            
            choixCase = ListeCase[numCase-1]
            
            self.deplacer_pion(joueur,self.plateau[choixCase[0],choixCase[1]] , pion)
            joueur.doubleD = [False,None]
             
            
        elif choix == 4 :
             
             
             ListeSens = ['h','b','g','d']
             
             
             if adversaire.doubleD[0] == True and adversaire.doubleD[1] != None :
                 self.deplacer_carre_x2(joueur, adversaire)
                 
             elif adversaire.doubleD[0] == False :
                 if (self.plateau.i_vide, self.plateau.j_vide) == (0,1) or (self.plateau.i_vide, self.plateau.j_vide) == (1,0) or (self.plateau.i_vide, self.plateau.j_vide) == (1,2) or (self.plateau.i_vide, self.plateau.j_vide) == (2,1) :
                     self.deplacer_carre_x2(joueur,adversaire,sens=None)
                     #affecter choix sens diff de None  quand on a le choix 
                 elif (self.plateau.i_vide, self.plateau.j_vide) == (0,0) or (self.plateau.i_vide, self.plateau.j_vide) == (0,2) or (self.plateau.i_vide, self.plateau.j_vide) == (2,0) or (self.plateau.i_vide, self.plateau.j_vide) == (2,2) :
                    
                    choixSens = None
                    Deplacement = False
                    while (Deplacement == False or choixSens not in ListeSens) :
                     
                     choixSens = input(" Selectionner le sens parmis la liste {} :\n".format(ListeSens))
                     Deplacement = self.deplacer_carre_x2(joueur,adversaire, sens=choixSens)
                    
             joueur.doubleD[0] = True
             
             
             
    
    # def test(self):
    #     self.choix_action_joueur(self.j1, self.j2)
    #     self.plateau.afficherPlateau()
    #     self.choix_action_joueur(self.j1, self.j2)
    #     self.plateau.afficherPlateau()
    #     self.j1.pions_poses[0].x=4
    #     print(self.plateau[1,1].pion.x)
        
        
        # noeud = Node(self.j1,self.j2,0,self.plateau,None,None)
        # noeud.actions_possibles()
        # noeud.results()
        # noeud.creer_enfants(noeud.profondeur)
        
        # action = minimax(noeud)
        # print('num :',action.numAction)
        # print('coord :',(action.x,action.y))
        # print('numPion :', action.numPion)
        # print('sens :',action.sens)
        
        # som = 0
        # for enfant in noeud.ListeEnfants :
        #     som += len(enfant.ListeEnfants)
            
        # print(som)
        # enfant = noeud.ListeEnfants[0]
        # enfant.jeu.plateau.afficherPlateau()
        # print(enfant.ListeEnfants)
        # for action,enfant in list(zip(noeud.ListeAction,noeud.ListeEnfants)) :
        #     print('num :' ,action.numAction)
        #     print('coord : ', (action.x,action.y))
        #     print(' numero pion : ', action.numPion)
        #     print('sens depl :', action.sens)
        #     print("plateau :\n")
        #     enfant.jeu.plateau.afficherPlateau()
        #     print(enfant.adversaire.doubleD)
        #     print(enfant)
    
    
    
    def choix_action_ia(self,joueur,adversaire):
        
        print(joueur.nom,"joue: ")
        
        noeud = Node(joueur,adversaire,0,self.plateau,None,None)
        noeud.actions_possibles()
        noeud.results()#nous donne tous les moves de joueur
        noeud.creer_enfants(noeud.profondeur)
        action = minimax(noeud)
        
       
        
        if action.numAction == 1 :
            self.deplacement_carre(self.plateau[action.x,action.y])
            joueur.doubleD[1] == False
        elif action.numAction == 2 :
            self.poser_pion(joueur, self.plateau[action.x,action.y])
            joueur.doubleD[1] == False
        elif action.numAction == 3 :
            self.deplacer_pion(joueur, self.plateau[action.x,action.y], joueur.pions_poses[action.numPion-1])
            joueur.doubleD[1] == False
        elif action.numAction == 4 :
            self.deplacer_carre_x2(joueur, adversaire,sens = action.sens)
            joueur.doubleD[0] == True
            
        
#%%


def victoire(joueur,plateau):
    """
    verifie si un des joueurs a gagner cad aligné 3 pions de même couleur
    """
    
    from carre_noir import CarreNoir
    i_vide = plateau.i_vide
    j_vide = plateau.j_vide
    plateau[i_vide, j_vide]=CarreNoir(i_vide,j_vide)
    couleur = joueur.couleur
    
    win = False
    
    
    # première ligne
    if (plateau[0,0].pion != None and plateau[0,1].pion != None and plateau[0,2].pion != None and plateau[0,0].pion.couleur == plateau[0,1].pion.couleur == plateau[0,2].pion.couleur == couleur ):
        
        win = True
            
        
    # deuxième ligne
    if (plateau[1,0].pion != None and plateau[1,1].pion != None and plateau[1,2].pion != None and plateau[1,0].pion.couleur == plateau[1,1].pion.couleur == plateau[1,2].pion.couleur == couleur ):
        
        win = True
    
    # troisième  ligne
    if plateau[2,0].pion != None and plateau[2,1].pion != None and plateau[2,2].pion != None  and plateau[2,0].pion.couleur == plateau[2,1].pion.couleur == plateau[2,2].pion.couleur == couleur :
        
            win = True
        
    # première colonne
    if (plateau[0,0].pion != None and plateau[1,0].pion != None and plateau[2,0].pion != None and plateau[0,0].pion.couleur == plateau[1,0].pion.couleur == plateau[2,0].pion.couleur == couleur ):
        
        win = True
    
    # deuxième colonne
    if (plateau[0,1].pion != None and plateau[1,1].pion != None and plateau[2,1].pion != None and plateau[0,1].pion.couleur == plateau[1,1].pion.couleur == plateau[2,1].pion.couleur == couleur ):
        
        win = True
        
    # troisième colonne
    if (plateau[0,2].pion != None and plateau[1,2].pion != None and plateau[2,2].pion != None and plateau[0,2].pion.couleur == plateau[1,2].pion.couleur == plateau[2,2].pion.couleur == couleur ):
        
        win = True 
        
    #diagonale 1 (haut gauche -> bas droite)
    
    if (plateau[0,0].pion != None and plateau[1,1].pion != None and plateau[2,2].pion != None and plateau[0,0].pion.couleur == plateau[1,1].pion.couleur == plateau[2,2].pion.couleur == couleur ):
        
        win = True 
    
    
    #diagonale 2 (bas gauche -> haut droite)
    
    if (plateau[2,0].pion != None and plateau[1,1].pion != None and plateau[0,2].pion != None and plateau[2,0].pion.couleur == plateau[1,1].pion.couleur == plateau[0,2].pion.couleur == couleur ):
        
        win = True 
        
    plateau[i_vide, j_vide] = None 
    
    return win 


#%% Evaluation

import numpy as np


def evaluation_position_pion(joueur, plateau) :
    
    TabPoids = np.array([[3,2,3],[2,4,2],[3,2,3]])
    
    Poids = sum([TabPoids[pion.x,pion.y] for pion in joueur.pions_poses if pion != None])
    
    return Poids

def evaluation_nb_pion(joueur, plateau):
    
    return len([pion for pion in joueur.pions_poses if pion != None])


def evaluation_pion_aligne(joueur, plateau) :
    
    
    
    
    TabTest = np.pad(plateau.plateau,1)
    
    evaluation = 0
    score = 0
    for pion in joueur.pions_poses :
        if pion == None :
            continue;
        else :
            for k in range((pion.x+1)-1, (pion.x+1)+2):
                for l in range((pion.y+1)-1, (pion.y+1)+2):
                        
                         
                    
                         if TabTest[k,l] !=None and TabTest[k,l] != 0 and TabTest[k,l].pion != None and  TabTest[k,l].pion.couleur == joueur.couleur : 
                              
                             if k == pion.x+1 and l == pion.y+1 :
                                  pass;
                             else :
                                 score +=1
                                 
       
                              
       
    if score == 4 :
        if victoire(joueur, plateau) == True :
            
            evaluation = 1000              
                    
        else :
            evaluation = 2
    
    if score == 6 :
        
        evaluation = 2
    
    if score == 2 :
        evaluation = 1

                         
                
    return evaluation 
def evaluation_victoire(joueur, plateau) : 
    score = 0
    if victoire(joueur, plateau) == True :
        score = 1000
    return score
    
def evaluation_bloquer_entre(joueur,plateau):
    
    
    score = 0
       
    for i in range(3):
        
        if (plateau[1,i]!=None  and plateau[1,i].pion!= None and plateau[1,i].pion.couleur == joueur.couleur and plateau[0,i]!=None  and plateau[0,i].pion!= None and plateau[0,i].pion.couleur != joueur.couleur and plateau[2,i]!=None  and plateau[2,i].pion!= None and plateau[2,i].pion.couleur != joueur.couleur):
                   score = 50
            
        if (plateau[i,1]!=None  and plateau[i,1].pion!= None and plateau[i,1].pion.couleur == joueur.couleur and plateau[i,0]!=None  and plateau[i,0].pion!= None and plateau[i,0].pion.couleur != joueur.couleur and plateau[i,2]!=None  and plateau[i,2].pion!= None and plateau[i,2].pion.couleur != joueur.couleur):
                   score = 50
    return score


def evaluation_bloquer_aligné(joueur, plateau):
    score = 0
       
    for i in range(3):
        if (plateau[0,i]!=None  and plateau[0,i].pion!= None and plateau[0,i].pion.couleur == joueur.couleur and plateau[1,i]!=None  and plateau[1,i].pion!= None and plateau[0,i].pion.couleur != joueur.couleur and plateau[2,i]!=None  and plateau[2,i].pion!= None and plateau[2,i].pion.couleur != joueur.couleur):
                   score = 50
                   
        if (plateau[2,i]!=None  and plateau[2,i].pion!= None and plateau[2,i].pion.couleur == joueur.couleur and plateau[1,i]!=None  and plateau[1,i].pion!= None and plateau[1,i].pion.couleur != joueur.couleur and plateau[0,i]!=None  and plateau[0,i].pion!= None and plateau[0,i].pion.couleur != joueur.couleur):
                   score = 50
            
        if (plateau[i,0]!=None  and plateau[i,0].pion!= None and plateau[i,0].pion.couleur == joueur.couleur and plateau[i,1]!=None  and plateau[i,1].pion!= None and plateau[i,1].pion.couleur != joueur.couleur and plateau[i,2]!=None  and plateau[i,2].pion!= None and plateau[i,2].pion.couleur != joueur.couleur):
                   score = 50
                   
        if (plateau[i,2]!=None  and plateau[i,2].pion!= None and plateau[i,2].pion.couleur == joueur.couleur and plateau[i,1]!=None  and plateau[i,1].pion!= None and plateau[i,1].pion.couleur != joueur.couleur and plateau[i,0]!=None  and plateau[i,0].pion!= None and plateau[i,0].pion.couleur != joueur.couleur):
                   score = 50
    return score

#%% IA

from copy import deepcopy




class Action():
    
    def __init__(self, numAction, x, y, sens = None, numPion = None):
        
        self.numAction = numAction
        self.x = x
        self.y = y
        self.sens = sens
        self.numPion = numPion
        
          

class Node():
    
    
    def __init__(self, joueur, adversaire, profondeur, plateau, parent = None, actionParent = None) :
        
        self.profondeur = profondeur
        self.joueur = joueur
        self.adversaire = adversaire
        self.plateau = plateau
        
        
        self.ListeChoix = []
        self.ListeAction = []
        self.ListeEnfants = []
        
        self.parent = parent
        self.actionParent = actionParent
        
        self.jeu = Jouer(self.joueur,self.adversaire,self.plateau)
        self.score = None
        
       
    def actions_possibles(self):
        
        #1 : deplacer carré
        #2 : poser un pion
        #3 : deplacer pion
        #4 : double déplacement carré
        
        self.ListeChoix = [1,2,3,4]
        
        if self.joueur.pions_en_main == [None]*3 :
                self.ListeChoix[1] = None 
        
        #pas de pions poses
        if self.joueur.pions_poses == [None]*3 :
            self.ListeChoix[2] = None
        
        #condition double deplacement
        if (self.adversaire.doubleD[0] == True and self.adversaire.doubleD[1] == None) or (self.plateau.i_vide == 1 and self.plateau.j_vide == 1):
            self.ListeChoix[3]= None
        
        self.ListeChoix = [x for x in self.ListeChoix if x!= None]
        
        
    
    
    def results(self):
        
        for choix in self.ListeChoix :
            
            plateau = deepcopy(self.plateau)
            joueur = deepcopy(self.joueur)
            adversaire = deepcopy(self.adversaire)
            
            if choix == 1 :
                
                i_vide = plateau.i_vide +1
                j_vide = plateau.j_vide +1
                
                
                TabTest = np.pad(plateau.plateau,1)
                
                for k in range(i_vide-1, i_vide+2):
                    for l in range(j_vide-1, j_vide+2):
                       
                        
                            
                          if (k == i_vide and (l == (j_vide-1) or l == (j_vide+1))) :
                              
                              if TabTest[k,l] != 0 : 
                                  
                                  action = Action(1,k-1,l-1)
                                  self.ListeAction.append(action)
                              
                                  
                               
                          if (l == j_vide and (k ==(i_vide-1) or k == (i_vide+1))) :
                             
                              if TabTest[k,l] != 0 :
                                
                                action = Action(1,k-1,l-1)
                                self.ListeAction.append(action)
            
            
            elif choix == 2 :
                
                
                for i in range(3) :
                    for j in range(3):
                        
                        if plateau[i,j] != None and plateau[i,j].pion == None :
                            action = Action(2,i,j)
                            self.ListeAction.append(action)
            
            
            elif choix == 3 :
                
                for pion in joueur.pions_poses :
                    if pion == None :
                        continue;
                    else : 
                        numPion = pion.numero
                        
                        for i in range(3) :
                            for j in range(3):
                                
                                if plateau[i,j] != None and plateau[i,j].pion == None :
                                    action = Action(3,i,j,numPion = numPion)
                                    self.ListeAction.append(action)
                                
            
            elif choix == 4 :
                
                if adversaire.doubleD[0] == True and adversaire.doubleD[1] != None :
                        action = Action(4,None,None,sens = None)
                        self.ListeAction.append(action)
                 
                elif adversaire.doubleD[0] == False :
                    
                    if (plateau.i_vide, plateau.j_vide) == (0,1) or (plateau.i_vide, plateau.j_vide) == (1,0) or (plateau.i_vide, plateau.j_vide) == (1,2) or (plateau.i_vide, plateau.j_vide) == (2,1) :
                        action = Action(4,None,None,sens = None)
                        self.ListeAction.append(action)
                    
                    elif (plateau.i_vide, plateau.j_vide) == (0,0) :
                        
                        action1 = Action(4,None,None,'h')
                        action2 = Action(4,None,None,'g')
                        self.ListeAction.append(action1)
                        self.ListeAction.append(action2)
                    
                    
                    elif (plateau.i_vide, plateau.j_vide) == (0,2) :
                        
                        action1 = Action(4,None,None,'h')
                        action2 = Action(4,None,None,'d')
                        self.ListeAction.append(action1)
                        self.ListeAction.append(action2)
                        
                    elif (plateau.i_vide, plateau.j_vide) == (2,0) :
                            
                        action1 = Action(4,None,None,'b')
                        action2 = Action(4,None,None,'g')
                        self.ListeAction.append(action1)
                        self.ListeAction.append(action2)
                    
                       
                    elif (plateau.i_vide, plateau.j_vide) == (2,2) :
                            
                        action1 = Action(4,None,None,'b')
                        action2 = Action(4,None,None,'d')
                        self.ListeAction.append(action1)
                        self.ListeAction.append(action2)
              
                
                
       
                
    def creer_enfants(self,profondeur) :
        
        for action in self.ListeAction :
            if profondeur >=2 : 
                break;
                
            numAction = action.numAction
            
            
            jeu = deepcopy(self.jeu)
            
            if numAction == 1 :
                
                jeu.deplacement_carre(jeu.plateau[action.x,action.y])
                jeu.j1.doubleD = [False,None]
                plateauEnfant = jeu.plateau
                parent = Node(self.joueur, self.adversaire, self.profondeur, self.plateau, self.parent, self.actionParent)
                enfant = Node(jeu.j1,jeu.j2,profondeur+1,plateauEnfant,parent,action)
                enfant.actions_possibles()
                enfant.results()
                enfant.creer_enfants(enfant.profondeur)
                self.ListeEnfants.append(enfant)
                

            elif numAction == 2 :
                
                jeu.poser_pion(jeu.j1, jeu.plateau[action.x,action.y])
                jeu.j1.doubleD = [False,None]
                plateauEnfant = jeu.plateau
                parent = Node(self.joueur, self.adversaire, self.profondeur, self.plateau, self.parent, self.actionParent)
                enfant = Node(jeu.j1,jeu.j2,profondeur+1,plateauEnfant,parent,action)                #enfant.plateau.afficherPlateau()
                enfant.actions_possibles()
                enfant.results()
                enfant.creer_enfants(enfant.profondeur)
                self.ListeEnfants.append(enfant)

            elif numAction == 3 :
                
               
                jeu.deplacer_pion(jeu.j1,jeu.plateau[action.x,action.y] , jeu.j1.pions_poses[action.numPion-1])
                plateauEnfant = jeu.plateau
                jeu.j1.doubleD = [False,None]
              
                parent = Node(self.joueur, self.adversaire, self.profondeur, self.plateau, self.parent, self.actionParent)
                enfant = Node(jeu.j1,jeu.j2,profondeur+1,plateauEnfant,parent,action)
               
                enfant.actions_possibles()
                enfant.results()
                enfant.creer_enfants(enfant.profondeur)
                self.ListeEnfants.append(enfant)

            elif numAction == 4 :
                
                
                jeu.deplacer_carre_x2(jeu.j1,jeu.j2,sens= action.sens)
                jeu.j1.doubleD[0] = True
                plateauEnfant = self.jeu.plateau
               
                parent = Node(self.joueur, self.adversaire, self.profondeur, self.plateau, self.parent, self.actionParent)
                enfant = Node(jeu.j1,jeu.j2,profondeur+1,plateauEnfant,parent,action)
              
                enfant.actions_possibles()
                enfant.results()
                enfant.creer_enfants(enfant.profondeur)
                self.ListeEnfants.append(enfant)

#%%

import random

def minimax(noeud):
    
    ListeBestNoeudProfondeur1 = []
    
    for enfant in noeud.ListeEnfants:
        
        ListeBestNoeudProfondeur2 = []
        
        for enfant2 in enfant.ListeEnfants :
            
            
            scoreNoeud =  evaluation_nb_pion(enfant2.adversaire, enfant2.plateau)
            scoreNoeud += evaluation_position_pion(enfant2.adversaire, enfant2.plateau)
            scoreNoeud += evaluation_pion_aligne(enfant2.adversaire, enfant2.plateau)
            scoreNoeud += evaluation_bloquer_aligné(enfant2.adversaire, enfant2.plateau)
            scoreNoeud += evaluation_bloquer_entre(enfant2.adversaire, enfant2.plateau)
            scoreNoeud += evaluation_victoire(enfant2.adversaire, enfant2.plateau)
            
            enfant2.score = scoreNoeud
            ListeBestNoeudProfondeur2.append(enfant2)
        
        
        ListeBestNoeudProfondeur2.sort(key= lambda x : x.score)
        
        BestScore2 = ListeBestNoeudProfondeur2[0].score
       
        
        ListeBestNodes2 = [el for el in ListeBestNoeudProfondeur2 if el.score == BestScore2]
      
        if len(ListeBestNodes2) > 1 :
        
            random.shuffle(ListeBestNodes2)
        ListeBestNoeudProfondeur1.append(ListeBestNodes2[0])
    
    ListeBestNoeudProfondeur1.sort(key= lambda x : x.score)
    
    BestScore = ListeBestNoeudProfondeur1[-1].score
    
   
    ListeBestNodes = [el for el in ListeBestNoeudProfondeur1 if el.score == BestScore]
    if len(ListeBestNodes) > 1 :
        
        random.shuffle(ListeBestNodes)
    
    NoeudFinal = ListeBestNodes[0].parent
    
    
    
    return NoeudFinal.actionParent
    
    
    
    
    
 ###------------essai d'une fonction qui minimise plutôt qui de qui maximise------------
 
 
# def minimax_minimiser(noeud):
    
#     ListeBestNoeudProfondeur1 = []
    
#     for enfant in noeud.ListeEnfants:
        
#         ListeBestNoeudProfondeur2 = []
        
#         for enfant2 in enfant.ListeEnfants :
            
#             scoreNoeud =  evaluation_nb_pion(enfant2.joueur, enfant2.plateau)
#             scoreNoeud += evaluation_position_pion(enfant2.joueur, enfant2.plateau)
#             scoreNoeud += evaluation_pion_aligne(enfant2.joueur, enfant2.plateau)
#             scoreNoeud += evaluation_bloquer_aligné(enfant2.joueur, enfant2.plateau)
#             scoreNoeud += evaluation_bloquer_entre(enfant2.joueur, enfant2.plateau)
            
#             enfant2.score = scoreNoeud
#             ListeBestNoeudProfondeur2.append(enfant2)
        
        
#         ListeBestNoeudProfondeur2.sort(key= lambda x : x.score)
        
#         WorstScore2 = ListeBestNoeudProfondeur2[-1].score
#         ListeBestNodes2 = [el for el in ListeBestNoeudProfondeur2 if el.score == WorstScore2]
#         if len(ListeBestNodes2) > 1 :
        
#             random.shuffle(ListeBestNodes2)
#         ListeBestNoeudProfondeur1.append(ListeBestNodes2[0])
    
#     ListeBestNoeudProfondeur1.sort(key= lambda x : x.score)
#     print('Liste1',[x.score for x in ListeBestNoeudProfondeur1])
#     print('Liste2',[x.score for x in ListeBestNoeudProfondeur2])
#     WorstScore = ListeBestNoeudProfondeur1[0].score
    
#     print(WorstScore)
#     ListeBestNodes = [el for el in ListeBestNoeudProfondeur1 if el.score == WorstScore]
#     if len(ListeBestNodes) > 1 :
        
#         random.shuffle(ListeBestNodes)
    
#     NoeudFinal = ListeBestNodes[0].parent
    
    
#     return NoeudFinal.actionParent
    
    
       
    
    
