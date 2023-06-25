import random

def cristal(grille):
    nouvelles_valeurs = []
    for ligne in grille:
        for element in ligne:
            if element != 0 and element != -1 and element != -2 and element not in nouvelles_valeurs:
                nouvelles_valeurs.append(element)
    val = random.choice(nouvelles_valeurs)
    print (val)
    print (nouvelles_valeurs)
    for i, ligne in enumerate(grille):
        for j, element in enumerate(ligne):
            if element == val:
                return i, j