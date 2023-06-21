import pygame
import random
import time 
from tir import * 
from test import partie_finie  
from finpartie import *



def affGrille(grille_pla, grille_tir_pla, score_player, score_ia, bateaux_ia, tirs_ia):
    pygame.init()

    # Définir les dimensions de la fenêtre
    largeur = 1250
    largeur_grille = 600
    hauteur = 650
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("Affichage de la Grille")

    # Couleurs
    COULEUR_FOND = (255, 255, 255)
    COULEUR_GRILLE = (0, 0, 0)
    COULEUR_BATEAU = (0, 0, 255)
    ROUGE = (255, 0, 0)
    GRIS = (128, 128, 128)

    # Dimensions de la grille
    nb_lignes = len(grille_pla)
    nb_colonnes = len(grille_pla[0])
    taille_case = largeur_grille // nb_colonnes

    # Initialiser les cases choisies
    cases_choisies = [[False] * nb_colonnes for _ in range(nb_lignes)]

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                colonne = (pos[0] - 650) // taille_case
                ligne = (pos[1] - 50) // taille_case

                
                # print(ligne, colonne)
                print(bateaux_ia)
                if 0 <= ligne < nb_lignes and 0 <= colonne < nb_colonnes:
                    print("Vous avez tiré en", ligne, colonne)
                    if tir(ligne, colonne, bateaux_ia)==True: 
                        print("Touché !")
                        grille_tir_pla[ligne][colonne] = 1  # Mettre à jour la grille de tir
                        bateaux_ia[ligne][colonne] = 2

                    else:
                        print("Raté !")
                        grille_tir_pla[ligne][colonne] = 0  # Mettre à jour la grille de tir
                        bateaux_ia[ligne][colonne] = -1

                    # pygame.display.flip()

                    #Tour de l'ordinateur

                    # pygame.event.wait()
                    # time.sleep(1)


                    ligne = random.randint(0,9)
                    colonne = random.randint(0,9)
                    while tirs_ia[ligne][colonne] != -1:
                        ligne = random.randint(0,9)
                        colonne = random.randint(0,9)
                    if tir(ligne, colonne, grille_pla)==True: 
                        print("L'ordinateur vous à touché !")
                        grille_pla[ligne][colonne] = 2  # Mettre à jour la grille de tir
                        tirs_ia[ligne][colonne] = 1

                    else:
                        print("L'ordinateur vous à raté !")
                        grille_pla[ligne][colonne] = -1  # Mettre à jour la grille de tir
                        tirs_ia[ligne][colonne] = 0
                    # print(ligne, colonne)
                if finpartie(grille_pla, bateaux_ia)==True:
                    running = False
                    print("Partie finie !")
                else: 
                    print("pas fini")
         

        # Effacer l'écran
        fenetre.fill(COULEUR_FOND)

        # Dessiner la grille bateau
        for ligne in range(nb_lignes):
            for colonne in range(nb_colonnes):
                x = colonne * taille_case
                y = ligne * taille_case + 50

                if grille_pla[ligne][colonne] == 1:
                    pygame.draw.rect(fenetre, COULEUR_BATEAU, (x, y, taille_case, taille_case))
                elif grille_pla[ligne][colonne] == 0:
                    pygame.draw.rect(fenetre, COULEUR_GRILLE, (x, y, taille_case, taille_case), 1)
                elif grille_pla[ligne][colonne] == -1:
                    pygame.draw.rect(fenetre, GRIS, (x, y, taille_case, taille_case))
                elif grille_pla[ligne][colonne] == 2:
                    pygame.draw.rect(fenetre, ROUGE, (x, y, taille_case, taille_case))


        # Dessiner la grille de tirs
        for ligne in range(nb_lignes):
            for colonne in range(nb_colonnes):
                x = colonne * taille_case + 650
                y = ligne * taille_case + 50

                if grille_tir_pla[ligne][colonne] == 1:
                    pygame.draw.rect(fenetre, COULEUR_BATEAU, (x, y, taille_case, taille_case))
                    cases_choisies[ligne][colonne] = True
                elif grille_tir_pla[ligne][colonne] == -1:
                    pygame.draw.rect(fenetre, COULEUR_GRILLE, (x, y, taille_case, taille_case), 1)
                elif grille_tir_pla[ligne][colonne] == 0:
                    pygame.draw.rect(fenetre, GRIS, (x, y, taille_case, taille_case))
                    cases_choisies[ligne][colonne] = True


        police = pygame.font.Font(None, 24)

        # Afficher le texte d'information
        info_texte = "Votre grille de bateau :"
        texte_info = police.render(info_texte, True, (0, 0, 0))
        fenetre.blit(texte_info, (10, 20))

        # Afficher le texte d'information
        info_texte = "Votre grille de tir :"
        texte_info = police.render(info_texte, True, (0, 0, 0))
        fenetre.blit(texte_info, (660, 20))



        # Mettre à jour l'affichage
        pygame.display.flip()


#  if partie_finie(grille_pla, grille_tir_pla):
#                     running = False


    # Quitter Pygame
    pygame.quit()
