import pygame
import random
import time 
from tir import * 
from test import partie_finie  
from finpartie import *
from checkcoule import *



def affGrille(grille_pla, grille_tir_pla, score_player, score_ia, bateaux_ia, tirs_ia):
    pygame.init()

    # Définir les dimensions de la fenêtre
    largeur = 1050
    largeur_grille = 500
    hauteur = 550
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

    # Variables pour afficher le message
    afficher_message_pla = 0
    debut_affichage_message_pla = 0 

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                colonne = (pos[0] - 550) // taille_case
                ligne = (pos[1] - 50) // taille_case

                # while grille_tir_pla[ligne][colonne] != -1:
                #     ligne = random.randint(0,9)
                #     colonne = random.randint(0,9)

                # print(ligne, colonne)
                # print(bateaux_ia)
                if 0 <= ligne < nb_lignes and 0 <= colonne < nb_colonnes:
                    if grille_tir_pla[ligne][colonne] == -1:
                        print("Vous avez tiré en", ligne, colonne)
                        if tir(ligne, colonne, bateaux_ia)==True: 
                            print("Touché !")
                            grille_tir_pla[ligne][colonne] = 1  # Mettre à jour la grille de tir

                            if checkcoule(bateaux_ia, bateaux_ia[ligne][colonne]):
                                # print("jbdvoibfibfdiù")
                                afficher_message_pla = 3
                                debut_affichage_message_pla = time.time()
                            else:
                                afficher_message_pla = 1
                                debut_affichage_message_pla = time.time()

                            bateaux_ia[ligne][colonne] = -2
                            #Afficher "Touché !"

                        else:
                            print("Raté !")
                            grille_tir_pla[ligne][colonne] = 0  # Mettre à jour la grille de tir
                            bateaux_ia[ligne][colonne] = -1
                            afficher_message_pla = 2
                            debut_affichage_message_pla = time.time()

                        # pygame.display.flip()



                        #Tour de l'ordinateur
                        ligne = random.randint(0,9)
                        colonne = random.randint(0,9)
                        while tirs_ia[ligne][colonne] != -1:
                            ligne = random.randint(0,9)
                            colonne = random.randint(0,9)
                        if tir(ligne, colonne, grille_pla)==True: 
                            print("L'ordinateur vous à touché !")
                            grille_pla[ligne][colonne] = -2  # Mettre à jour la grille de tir
                            tirs_ia[ligne][colonne] = 1

                        else:
                            print("L'ordinateur vous à raté !")
                            grille_pla[ligne][colonne] = -1  # Mettre à jour la grille de tir
                            tirs_ia[ligne][colonne] = 0
                        # print(ligne, colonne)
                    else:
                        print("Vous avez déjà tiré en", ligne, colonne, ", choisissez une autre case")


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

                if 1<=grille_pla[ligne][colonne]<=5:
                    pygame.draw.rect(fenetre, COULEUR_BATEAU, (x, y, taille_case, taille_case))
                elif grille_pla[ligne][colonne] == 0:
                    pygame.draw.rect(fenetre, COULEUR_GRILLE, (x, y, taille_case, taille_case), 1)
                elif grille_pla[ligne][colonne] == -1:
                    pygame.draw.rect(fenetre, GRIS, (x, y, taille_case, taille_case))
                elif grille_pla[ligne][colonne] == -2:
                    pygame.draw.rect(fenetre, ROUGE, (x, y, taille_case, taille_case))


        # Dessiner la grille de tirs
        for ligne in range(nb_lignes):
            for colonne in range(nb_colonnes):
                x = colonne * taille_case + 550
                y = ligne * taille_case + 50

                if grille_tir_pla[ligne][colonne]==1:
                    pygame.draw.rect(fenetre, COULEUR_BATEAU, (x, y, taille_case, taille_case))
                    cases_choisies[ligne][colonne] = True
                elif grille_tir_pla[ligne][colonne] == -1:
                    pygame.draw.rect(fenetre, COULEUR_GRILLE, (x, y, taille_case, taille_case), 1)
                elif grille_tir_pla[ligne][colonne] == 0:
                    pygame.draw.rect(fenetre, GRIS, (x, y, taille_case, taille_case))
                    cases_choisies[ligne][colonne] = True


        police = pygame.font.Font(None, 24)
        police_message = pygame.font.Font(None, 36)

        # Afficher le texte d'information
        info_texte = "Votre grille de bateau :"
        texte_info = police.render(info_texte, True, (0, 0, 0))
        fenetre.blit(texte_info, (10, 20))

        # Afficher le texte d'information
        info_texte = "Votre grille de tir :"
        texte_info = police.render(info_texte, True, (0, 0, 0))
        fenetre.blit(texte_info, (560, 20))

        # Touché / coulé joueur 
        if afficher_message_pla==1:
            message_texte = "Touché !"
            texte_message = police_message.render(message_texte, True, (255, 0, 0))
            texte_rect = texte_message.get_rect(center=(800, hauteur // 2))
            fenetre.blit(texte_message, texte_rect)
            # Vérifier si le temps d'affichage du message est écoulé
            if time.time() - debut_affichage_message_pla > 0.5:
                afficher_message_pla = 0
        elif afficher_message_pla==2:
            message_texte = "Raté !"
            texte_message = police_message.render(message_texte, True, (255, 0, 0))
            texte_rect = texte_message.get_rect(center=(800, hauteur // 2))
            fenetre.blit(texte_message, texte_rect)
            # Vérifier si le temps d'affichage du message est écoulé
            if time.time() - debut_affichage_message_pla > 0.5:
                afficher_message_pla = 0
        elif afficher_message_pla==3:
            message_texte = "Coulé !"
            texte_message = police_message.render(message_texte, True, (255, 0, 0))
            texte_rect = texte_message.get_rect(center=(800, hauteur // 2))
            fenetre.blit(texte_message, texte_rect)
            # Vérifier si le temps d'affichage du message est écoulé
            if time.time() - debut_affichage_message_pla > 0.5:
                afficher_message_pla = 0


        # Mettre à jour l'affichage
        pygame.display.flip()


#  if partie_finie(grille_pla, grille_tir_pla):
#                     running = False


    # Quitter Pygame
    pygame.quit()
