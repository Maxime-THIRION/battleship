import pygame
from Function import *
import random
from test import *

def play(largeur, hauteur):

    bateaux_player = init_grille(0)
    tirs_player = init_grille(-1)

    bateaux_ia = init_grille(0)
    bateaux_ia = Placement_bateaux_aleatoire(bateaux_ia)
    tirs_ia = init_grille(-1)
    
    score_player = 25
    score_ia = 25

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Votre code à exécuter lorsque la touche "Entrée" est pressée
                print("ok !")
                
            
            # Afficher les autres lignes de texte en utilisant la fonction afficher_texte()
            background = pygame.image.load("images/background2.jpeg").convert()
            background = pygame.transform.scale(background, (largeur, hauteur))
            screen.blit(background, (0, 0))

            pygame.display.flip()

            Placement_bateau_player(bateaux_player)

            



    pygame.quit()

