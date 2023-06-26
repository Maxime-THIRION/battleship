# importation des bibliothèques
import random
# from affGrille import * 

# définition des grilles de jeu
COLONNES = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}

NAVIRES = {'Porte-avion':5,'Croiseur':4,'Contre-torpilleur1':3, 'Contre-torpilleur2':3, 'Sous-marin':2}
SENS = ['H','V']

# initialisation de la grille de départ
def init_grille(symbole):
	grille=[]
	for i in range(10):
		grille.append([])
		for j in range (10):
			grille[i].append(symbole)
	return grille
            
            
def Init_placement_bateaux(c, l, bateau, sens, grille, joueur, val):
    taille=NAVIRES[bateau]
    if sens == 1:
        if c+(taille-1)<10 and c<=(10-taille):
            c1=c
            for i in range (taille):
                grille[l][c1]=val
                # Sauvegarde_placement(c1, l, bateau, joueur)
                c1+=1
            return grille
    elif sens == 2:
        if l+(taille-1)<10 and l<=(10-taille):
            l1 = l
            for i in range(taille):
                grille[l1][c]=val
                # Sauvegarde_placement(c, l1, bateau, joueur)
                l1+=1
            return grille
    else:
        print("/!\ Sens inconnu /!\ ")
        

def Placement_bateaux_aleatoire(grille):
        p=1
        for bateau in NAVIRES:
            taille = NAVIRES[bateau]
            possible = 0
            while possible != 1:
                x = random.randint(0,9)
                y = random.randint(0,9)
                sens = random.randint(1,2)
                possible = Placement_possible(x, y, taille, sens, grille)
            Init_placement_bateaux(x, y, bateau, sens, grille, "ia", p)
            p=p+1
        return grille
            


def Placement_possible(c, l, taille, sens, grille):

	if sens == 1:
		if c+(taille-1)<10 and c<=(10-taille):
			c1 = c
			cpt = 0
			possible = 1
			while cpt !=taille and possible ==1:
				possible = 0
				if grille[l][c1] == 0:
					possible = 1
					c1+=1
					cpt+=1
			return possible
		else:
			return 0

	if sens == 2:
		if l+(taille-1)<10 and l<=(10-taille):
			l1 = l
			cpt = 0
			possible = 1
			while cpt !=taille and possible ==1:
				possible = 0
				if grille[l1][l] == 0:
					possible = 1
					l1+=1
					cpt+=1
			return possible
		else:
			return 0