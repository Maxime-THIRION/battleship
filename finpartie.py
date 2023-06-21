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
            if case == 1:
                x=x+1

    for ligne in bateau_ia:
        for case in ligne:
            if case == 1:
                y=y+1

    if x==0 or y==0:
        return True
    else:
        return False

