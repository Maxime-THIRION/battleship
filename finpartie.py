import pygame 

def finpartie(bateau_pla, bateau_ia):
    # if 1 not in bateau_pla and 1 not in bateau_ia:
    #     return True
    # else:
    #     return False
    x=0
    y=0
    
    for ligne in bateau_pla:
        for case in ligne:
            if case == 1 or case == 2 or case == 3 or case == 4 or case == 5:
                x=x+1

    for ligne in bateau_ia:
        for case in ligne:
            if case == 1 or case == 2 or case == 3 or case == 4 or case == 5:
                y=y+1

    if y==0:
        return 'Victoire'
    elif x==0:
        return 'Défaite'

