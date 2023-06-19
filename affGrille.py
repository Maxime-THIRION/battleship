import pygame

def affGrille(grille_pla, grille_tir, score_player, score_ia):
    pygame.init()

    # Définir les dimensions de la fenêtre
    largeur = 1250
    largeur_grille = 600
    hauteur = 650
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("Affichage de la Grille")

    # Couleurs
    COULEUR_FOND = (255, 255, 255)
    COULEUR_RATE = (255, 0, 0)
    COULEUR_GRILLE = (0, 0, 0)
    COULEUR_BATEAU = (0, 0, 255)

    # Dimensions de la grille
    nb_lignes = len(grille_pla)
    nb_colonnes = len(grille_pla[0])
    taille_case = largeur_grille // nb_colonnes

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Effacer l'écran
        fenetre.fill(COULEUR_FOND)

        # Dessiner la grille bateau
        for ligne in range(nb_lignes):
            for colonne in range(nb_colonnes):
                x = colonne * taille_case
                y = ligne * taille_case + 50

                if grille_pla[ligne][colonne] == 1:
                    pygame.draw.rect(fenetre, COULEUR_BATEAU, (x, y, taille_case, taille_case))
                else:
                    pygame.draw.rect(fenetre, COULEUR_GRILLE, (x, y, taille_case, taille_case), 1)

        # Dessiner la grille de tirs
        for ligne in range(nb_lignes):
            for colonne in range(nb_colonnes):
                x = colonne * taille_case + 650
                y = ligne * taille_case + 50

                if grille_tir[ligne][colonne] == 1:
                    pygame.draw.rect(fenetre, COULEUR_BATEAU, (x, y, taille_case, taille_case))
                else:
                    pygame.draw.rect(fenetre, COULEUR_GRILLE, (x, y, taille_case, taille_case), 1)


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

    # Quitter Pygame
    pygame.quit()
