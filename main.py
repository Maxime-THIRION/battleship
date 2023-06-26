import pygame
from Homepage import *
from Rules import *
from Play import *
pygame.init()

# Définir les dimensions de la fenêtre
largeur = 1000
hauteur = 700
screen = pygame.display.set_mode((largeur, hauteur))


# Boucle principale pour gérer le changement de page
def main_loop(largeur, hauteur):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        current_page = home_page  # Commencer avec la première page

        while current_page is not None:
            page_result = current_page(largeur, hauteur)  # Exécuter la boucle de jeu de la page actuelle

            if page_result == 'rules':
                current_page = rules
            elif page_result == 'play':
                current_page = play

            
        
main_loop(largeur, hauteur)

# Quitter Pygame
pygame.quit()




