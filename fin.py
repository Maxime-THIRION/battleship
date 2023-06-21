import pygame 

def fin(largeur, hauteur):
    pygame.init()

    # Définir les dimensions de la fenêtre
    largeur = 500
    hauteur = 200
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("Fin de partie")

    # Couleurs
    COULEUR_FOND = (255, 255, 255)
    COULEUR_TEXTE = (0, 0, 0)

    # Effacer l'écran
    fenetre.fill(COULEUR_FOND)

    # Afficher le texte du gagnant
    police = pygame.font.Font(None, 48)
    texte = police.render(f"Victoire", True, COULEUR_TEXTE)
    texte_rect = texte.get_rect(center=(largeur // 2, hauteur // 2))
    fenetre.blit(texte, texte_rect)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Attendre la fermeture de la fenêtre
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Quitter Pygame
    pygame.quit()
