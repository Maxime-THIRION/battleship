import pygame

pygame.init()
largeur = 800
hauteur = 600
fenetre_principale = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Fenêtre Principale")

fenetre_secondaire = pygame.Surface((200, 200))

en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # Efface l'écran de la fenêtre principale
    fenetre_principale.fill((255, 255, 255))

    # Efface l'écran de la fenêtre secondaire
    fenetre_secondaire.fill((0, 0, 0))

    # Dessinez les éléments dans la fenêtre principale
    pygame.draw.rect(fenetre_principale, (255, 0, 0), (100, 100, 200, 200))

    # Dessinez les éléments dans la fenêtre secondaire
    pygame.draw.rect(fenetre_secondaire, (0, 255, 0), (50, 50, 100, 100))

    # Copiez la fenêtre secondaire sur la fenêtre principale aux coordonnées spécifiées
    fenetre_principale.blit(fenetre_secondaire, (300, 300))

    # Mettez à jour l'écran de la fenêtre principale
    pygame.display.flip()

# Quittez Pygame
pygame.quit()

