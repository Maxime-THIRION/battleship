import pygame
from Play import *
import time


COLONNES = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}

NAVIRES = {'Porte-avion':5,'Croiseur':4,'Contre-torpilleur1':3, 'Contre-torpilleur2':3, 'Sous-marin':2}
SENS = ['H','V']


def verifier_superposition(grille, colonne, ligne, taille, orientation):
    nb_lignes = len(grille)
    nb_colonnes = len(grille[0])
    if orientation == "Horizontal":
        for i in range(taille):
            if colonne + i >= nb_colonnes or grille[ligne][colonne + i] == 1:
                return True
    elif orientation == "Vertical":
        for i in range(taille):
            if ligne + i >= nb_lignes or grille[ligne + i][colonne] == 1:
                return True
    return False



# import pygame
def placement_bateaux():
    pygame.init()

    # Définir les dimensions de la fenêtre
    largeur = 1000
    hauteur = 700
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("Placement des Bateaux")

    # fond
    background = pygame.image.load("images/sonar.jpeg").convert()
    background = pygame.transform.scale(background, (largeur, hauteur))
    screen.blit(background, (0, 0))

    pygame.draw.rect(screen, (0, 0, 0), (110, 70, 420, 440))  # Dessine un rectangle pour le cadre du texte

    # Couleurs
    COULEUR_FOND = background
    COULEUR_GRILLE = (255, 165, 0)
    COULEUR_BATEAU = (0, 0, 255)
    COULEUR_TEXTE = (255, 165, 0)

    # Police de caractères
    police = pygame.font.Font(None, 24)

    # Dimensions de la grille
    nb_lignes = 10
    nb_colonnes = 10
    taille_case = 420 // nb_colonnes

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

    # Variables pour afficher le message
    afficher_message = False
    debut_affichage_message = 0

    # Boucle principale
    running = True
    while running:

        superposition = False  # Variable pour vérifier la superposition de bateaux

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not placement_termine:
                    # Récupérer les coordonnées de la case cliquée
                    x, y = event.pos
                    ligne = (y-100) // taille_case
                    colonne = x // taille_case

                    # while verifier_superposition(grille, colonne, ligne, taille_bateau, orientation_bateau):
                    #     print ("Veuillez choisir une autre case")
                    #     x, y = event.pos
                    #     ligne = (y - 150) // taille_case
                    #     colonne = x // taille_case

                    if verifier_superposition(grille, colonne, ligne, taille_bateau, orientation_bateau):
                        superposition = True  # Superposition détectée
                        print("Veuillez choisir une autre case")
                        afficher_message = True
                        debut_affichage_message = time.time() 
                        break  # Sortir de la boucle for
                    
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

        # Dessiner la grille
        for ligne in range(nb_lignes):
            for colonne in range(nb_colonnes):
                x = colonne * taille_case + 110
                y = ligne * taille_case + 100

                pygame.draw.rect(fenetre, COULEUR_GRILLE, (x, y, taille_case, taille_case), 1)

        # Dessiner les bateaux déjà placés
        for ligne in range(nb_lignes):
            for colonne in range(nb_colonnes):
                if grille[ligne][colonne] == 1:
                    x = colonne * taille_case + 110
                    y = ligne * taille_case + 100
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
            texte_confirmation = police.render("Placement terminé ! Appuyez sur Entrée", True, COULEUR_TEXTE)
            fenetre.blit(texte_confirmation, (20, 80))
        else :
            texte_confirmation = police.render("'v' pour placr verticalement et 'h' pour placer horizontalement ", True, COULEUR_TEXTE)
            fenetre.blit(texte_confirmation, (20, 80))

        # Afficher le message de superposition
        if afficher_message:
            message_texte = "Placement impossible !"
            texte_message = pygame.font.Font(None, 36).render(message_texte, True, (255, 0, 0))
            fenetre.blit(texte_message, ((largeur//2)-120, hauteur//2))
            # Vérifier si le temps d'affichage du message est écoulé
            if time.time() - debut_affichage_message > 1.5:
                afficher_message = False

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
