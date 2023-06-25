import pygame 

def tir(ligne, colonne, bateaux):
    # print (ligne, colonne)
    # print(bateaux[ligne][colonne])
    if 1<=bateaux[ligne][colonne]<=5:
        print("True")
        return True
    else:
        print("False")
        return False
