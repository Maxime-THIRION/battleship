import pygame
from Function import *


def victory(largeur, hauteur):
    pygame.init()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'fin'
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Votre code à exécuter lorsque la touche "Entrée" est pressée
                print("ok !")
                
            
            # Afficher les autres lignes de texte en utilisant la fonction afficher_texte()
            background = pygame.image.load("images/background2.jpeg").convert()
            background = pygame.transform.scale(background, (largeur, hauteur))
            

            pygame.display.flip()



def over(largeur, hauteur):
    pygame.init()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'fin'
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Votre code à exécuter lorsque la touche "Entrée" est pressée
                print("ok !")
                
            
            # Afficher les autres lignes de texte en utilisant la fonction afficher_texte()
            background = pygame.image.load("images/background2.jpeg").convert()
            background = pygame.transform.scale(background, (largeur, hauteur))
            screen.blit(background, (0, 0))

            pygame.display.flip()