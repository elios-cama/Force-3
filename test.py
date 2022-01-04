# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 12:06:54 2021

@author: hcama
"""


# print("###################")
        # for i in range(3) :
        #     print("#     #     #     #")
        #     print("#  {} #  {} #  {} #".format(plateau[i,0],plateau[i,1],plateau[i,2]))
        #     print("#     #     #     #")
        #     print("###################")

from Joueur import Joueur
from plateau import Plateau


from Jouer import Jouer,Node
joueur1 = Joueur("a",0)
joueur2 = Joueur("b",1)
plateau = Plateau()

partie = Jouer(joueur1,joueur2,plateau)
partie.test()


