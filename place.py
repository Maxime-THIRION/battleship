import pygame
from Play import *


COLONNES = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}

NAVIRES = {'Porte-avion':5,'Croiseur':4,'Contre-torpilleur1':3, 'Contre-torpilleur2':3, 'Sous-marin':2}
SENS = ['H','V']




# import pygame
def placement_bateaux():
    pygame.init()

    # Définir les dimensions de la fenêtre
    largeur = 700
    hauteur = 850
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("Placement des Bateaux")

    # Couleurs
    COULEUR_FOND = (255, 255, 255)
    COULEUR_GRILLE = (0, 0, 0)
    COULEUR_BATEAU = (0, 0, 255)
    COULEUR_TEXTE = (0, 0, 0)

    # Police de caractères
    police = pygame.font.Font(None, 24)

    # Dimensions de la grille
    nb_lignes = 10
    nb_colonnes = 10
    taille_case = largeur // nb_colonnes

    # Grille de la bataille navale
    grille = [[0] * nb_colonnes for _ in range(nb_lignes)]

    # Bateaux à placer
    bateaux = ['Porte-avion', 'Croiseur', 'Contre-torpilleur1', 'Contre-torpilleur2', 'Sous-marin']
    bateau_actuel = 0
    bateau_selectionne = bateaux[bateau_actuel]
    taille_bateau = NAVIRES[bateau_selectionne]
    orientation_bateau = "Horizontal"

    # Variables de contrôle du placement
    placement_termine = False

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not placement_termine:
                    # Récupérer les coordonnées de la case cliquée
                    x, y = event.pos
                    ligne = (y-150) // taille_case
                    colonne = x // taille_case
                    
                    # Placer le bateau à l'emplacement choisi
                    if ligne < nb_lignes and colonne < nb_colonnes:
                        if orientation_bateau == "Horizontal" and colonne + taille_bateau <= nb_colonnes:
                            grille = Init_placement_bateaux(colonne, ligne, bateau_selectionne, 1, grille, 'player')
                            placement_termine = True
                        elif orientation_bateau == "Vertical" and ligne + taille_bateau <= nb_lignes:
                            grille = Init_placement_bateaux(colonne, ligne, bateau_selectionne, 2, grille, 'player')
                            placement_termine = True

            elif event.type == pygame.KEYDOWN:
                if not placement_termine:
                    if event.key == pygame.K_h:
                        orientation_bateau = "Horizontal"
                    elif event.key == pygame.K_v:
                        orientation_bateau = "Vertical"

        # Effacer l'écran
        fenetre.fill(COULEUR_FOND)

        # Dessiner la grille
        for ligne in range(nb_lignes):
            for colonne in range(nb_colonnes):
                x = colonne * taille_case
                y = ligne * taille_case + 150

                pygame.draw.rect(fenetre, COULEUR_GRILLE, (x, y, taille_case, taille_case), 1)

        # Dessiner les bateaux déjà placés
        for ligne in range(nb_lignes):
            for colonne in range(nb_colonnes):
                if grille[ligne][colonne] == 1:
                    x = colonne * taille_case
                    y = ligne * taille_case + 150
                    pygame.draw.rect(fenetre, COULEUR_BATEAU, (x, y, taille_case, taille_case))

        # Afficher le bateau à placer
        # x = largeur - 200
        # y = hauteur - 100
        # pygame.draw.rect(fenetre, COULEUR_BATEAU, (x, y, taille_case * taille_bateau, taille_case))

        # Afficher le texte d'information
        info_texte = f"Placez le bateau : {bateau_selectionne} ({taille_bateau} cases)"
        texte_info = police.render(info_texte, True, COULEUR_TEXTE)
        fenetre.blit(texte_info, (20, 20))

        # Afficher le texte d'orientation
        orientation_texte = f"Orientation : {orientation_bateau}"
        texte_orientation = police.render(orientation_texte, True, COULEUR_TEXTE)
        fenetre.blit(texte_orientation, (20, 50))

        # Afficher le texte de confirmation
        if placement_termine:
            texte_confirmation = police.render("Placement terminé !", True, COULEUR_TEXTE)
            fenetre.blit(texte_confirmation, (20, 80))

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Passer au bateau suivant ou terminer le placement
        if placement_termine:
            bateau_actuel += 1
            if bateau_actuel < len(bateaux):
                bateau_selectionne = bateaux[bateau_actuel]
                taille_bateau = NAVIRES[bateau_selectionne]
                orientation_bateau = "Horizontal"
                placement_termine = False
            else:
                # running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    running = False
                # print(grille)

    # Quitter Pygame
    pygame.quit()

    return grille
