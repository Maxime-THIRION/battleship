import pygame 

def tir(ligne, colonne, bateaux):
    # print (ligne, colonne)
    # print(bateaux[ligne][colonne])
    if bateaux[ligne][colonne] == 1:
        print("True")
        return True
    else:
        print("False")
        return False
