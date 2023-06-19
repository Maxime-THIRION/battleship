import pygame
from bouton import *  # Importer votre propre module 'bouton'
from test import *  # Importer votre propre module 'test'
from pygame.locals import *
from Function import *  # Importer votre propre module 'Function'

def home_page(largeur, hauteur):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                position = pygame.mouse.get_pos()
                if button.check_clic(position):  # Utilisation d'une méthode 'check_clic' sur un objet 'button'
                    print("check click ok")  # Afficher un message lorsque le bouton est cliqué
                    return 'rules'  # Retourner 'rules' lorsque le bouton est cliqué

        background = pygame.image.load("images/background.jpeg").convert()
        background = pygame.transform.scale(background, (largeur, hauteur))

        button = Bouton((largeur-150)/2 , (hauteur+200)/2, 150, 50, "PLAY")  # Création d'un objet 'Bouton'

        screen.blit(background, (0, 0))  # Affichage de l'arrière-plan

        display_title("- BattleShip -")  # Afficher un titre

        display_text("Swim in dangerous water", "bebas_neue/BebasNeue-Regular.ttf", 24, 400, 375, 255, 255, 255)  # Afficher du texte

        button.display()  # Afficher le bouton

        pygame.display.flip()  # Mettre à jour l'affichage

    pygame.quit()  # Quitter Pygame à la fin de la boucle while