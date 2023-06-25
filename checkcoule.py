import pygame 

def checkcoule(grille, bateau):
    x=0
    
    for ligne in grille:
        for case in ligne:
            if case == bateau:
                print("test checkcoule")
                x=x+1

    if x>1:
        return False
    else:
        return True

