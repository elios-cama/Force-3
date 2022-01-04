# -*- coding: utf-8 -*-
"""
Created by Elios Cama, Christian Do, Nathan Damette
2022
"""

from parties import IAvIA, JvIA, JvJ


def main():
    
    print("------------Bienvenue dans Force 3-------------\n\n\n")
    print("Veuillez choisir un mode de jeu")
    print("1: Joueur contre Joueur\n2: Joueur contre IA\n3: IA contre IA")
    
    choix_partie = int(input("\n---------Faites votre choix : \n"))
    

    if choix_partie == 1:
        JvJ()
        
    if choix_partie == 2:
        JvIA()
    if choix_partie == 3 :
        IAvIA()
    
    
#%%


if __name__ == "__main__":
    main()
