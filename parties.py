
from Joueur import Joueur
from plateau import Plateau
from Jouer import Jouer, victoire

dictCouleur ={
    "Rouge" : 0,
    "Bleu" : 1
    }

#%% 

def JvJ():
    
    print(" Joueur vs Joueur ")
    
    nameJoueur1 = input("Name of joueur 1 :\n")
    nameJoueur2 = input("Name of joueur 2 :\n")
    
    couleurJoueur1 = dictCouleur["Rouge"]
    couleurJoueur2 = dictCouleur["Bleu"]
    
    joueur1 = Joueur(nameJoueur1, couleurJoueur1)
    joueur2 = Joueur(nameJoueur2, couleurJoueur2)
    
    
    plateau = Plateau()
    jouer = Jouer(joueur1, joueur2, plateau)
    
    
    win = False 
    while win == False:
        
        plateau.afficherPlateau()
        print('\n')
        jouer.choix_action_joueur(joueur1, joueur2)
        win = victoire(joueur1,plateau)
        
        if win == True :
            print("Le joueur1 a gagné la partie")
            break
        
        else :
            
            plateau.afficherPlateau()
            print('\n')
            jouer.choix_action_joueur(joueur2, joueur1)
            win = victoire(joueur2,plateau)
            
            if win == True :
                print("Le joueur2 a gagné la partie")
                break

    
#%%

def JvIA():
    print(" Joueur vs IA ")
    print(" Joueur vs Joueur ")

    nameJoueur1 = input("Name of joueur 1 :\n")
    nameJoueur2 = "IA2"

    couleurJoueur1 = dictCouleur["Rouge"]
    couleurJoueur2 = dictCouleur["Bleu"]

    joueur1 = Joueur(nameJoueur1, couleurJoueur1)
    joueur2 = Joueur(nameJoueur2, couleurJoueur2)


    plateau = Plateau()
    jouer = Jouer(joueur1, joueur2, plateau)


    win = False 
    while win == False:

        plateau.afficherPlateau()
        print('\n')
        jouer.choix_action_joueur(joueur1, joueur2)
        win = victoire(joueur1,plateau)

        if win == True :
            print("Le joueur1 a gagné la partie")
            break

        else :

            plateau.afficherPlateau()
            print('\n')
            jouer.choix_action_ia(joueur2, joueur1)
            win = victoire(joueur2,plateau)

            if win == True :
                print("L'IA a gagné la partie")
                break

#%%
import time


def IAvIA():
    print(" IA vs IA ")
    
    nameJoueur1 = "IA1"
    nameJoueur2 = "IA2"
    
    couleurJoueur1 = dictCouleur["Rouge"]
    couleurJoueur2 = dictCouleur["Bleu"]
    
    joueur1 = Joueur(nameJoueur1, couleurJoueur1)
    joueur2 = Joueur(nameJoueur2, couleurJoueur2)
    
    
    plateau = Plateau()
    jouer = Jouer(joueur1, joueur2, plateau)
    plateau.afficherPlateau()
    
    
    win = False 
    while win == False:
        
        
        time.sleep(0.1)
        print('\n')
        jouer.choix_action_ia(joueur1, joueur2)
        plateau.afficherPlateau()
        win = victoire(joueur1,plateau)
        
        if win == True :
            print("L'IA1 a gagné la partie")
            plateau.afficherPlateau()
            break
        
        else :
            
           
            time.sleep(0.1)
            print('\n')
            jouer.choix_action_ia(joueur2, joueur1)
            plateau.afficherPlateau()
            win = victoire(joueur2,plateau)
            
            if win == True :
                print("L'IA2 a gagné la partie")
                plateau.afficherPlateau()
                break
    
    
    





















