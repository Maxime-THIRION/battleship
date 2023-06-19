import pygame

# Définition des constantes pour les dimensions de la grille et des cases
LETTRES = ['A','B','C','D','E','F','G','H','I','J']
GRILLE_WIDTH = 400
GRILLE_HEIGHT = 400
CASE_SIZE = GRILLE_WIDTH // 10

# Définition des couleurs
COULEUR_FOND = (255, 255, 255)
COULEUR_GRILLE = (0, 0, 0)
COULEUR_CASE_VIDE = (255, 255, 255)
COULEUR_CASE_BATEAU = (0, 0, 0)
COULEUR_CASE_TIR_MANQUE = (255, 0, 0)
COULEUR_CASE_TIR_TOUCHE = (255, 255, 0)

def affichage_grille_bateau(bateaux):
    pygame.init()
    fenetre = pygame.display.set_mode((GRILLE_WIDTH, GRILLE_HEIGHT))
    pygame.display.set_caption("Affichage Grille Bateau")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fenetre.fill(COULEUR_FOND)

        numligne = 1
        while numligne <= 10:
            ligne = bateaux[numligne - 1]

            for colonne in range(10):
                case_x = colonne * CASE_SIZE
                case_y = numligne * CASE_SIZE

                if ligne[colonne] == 0:
                    pygame.draw.rect(fenetre, COULEUR_CASE_VIDE, (case_x, case_y, CASE_SIZE, CASE_SIZE))
                elif ligne[colonne] == 1:
                    pygame.draw.rect(fenetre, COULEUR_CASE_BATEAU, (case_x, case_y, CASE_SIZE, CASE_SIZE))
                elif ligne[colonne] == 'tirmanqué':
                    pygame.draw.rect(fenetre, COULEUR_CASE_TIR_MANQUE, (case_x, case_y, CASE_SIZE, CASE_SIZE))
                elif ligne[colonne] == 'tirtouché':
                    pygame.draw.rect(fenetre, COULEUR_CASE_TIR_TOUCHE, (case_x, case_y, CASE_SIZE, CASE_SIZE))

            numligne += 1

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()