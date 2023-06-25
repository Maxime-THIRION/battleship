import time
import pygame
from Function import *

def rules(largeur, hauteur):

    police = pygame.font.Font("bebas_neue/BebasNeue-Regular.ttf", 20)
    text = "> Rapel des regles. . > disposez les bateAux horizontalement ou verticalement. > Attention. > vous ne pouvez pas mettre deux bateaux l'un sur l'autre. > Vous disposez des bateaux suivants. >  1 Porte-avion (5 cases). > 1 Croiseur (4 cases). >  2 Contre-torpilleurs (3 cases). >  1 Sous-marin (2 cases). . . > Press enter to place your ships."
    phrases = split_phrases(text)  # Découpage du texte en phrases individuelles
    index_phrase = 0

    x = 125
    y = 80
    largeur_zone = 400
    hauteur_zone = 420
    # vitesse_affichage = 0.2  # Vitesse d'affichage du texte
    vitesse_affichage = 0.05  # Vitesse d'affichage du texte
    surface_texte = pygame.Surface((largeur_zone, hauteur_zone))  # Surface pour afficher le texte

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Votre code à exécuter lorsque la touche "Entrée" est pressée
                print("La touche Entrée a été pressée !")
                return 'play'  # Retourne 'play' lorsque la touche "Entrée" est pressée

        background = pygame.image.load("images/sonar.jpeg").convert()
        background = pygame.transform.scale(background, (largeur, hauteur))
        #screen.blit(background, (0, 0))  # Affiche l'arrière-plan

        pygame.draw.rect(screen, (0, 0, 0), (110, 70, 420, 440))  # Dessine un rectangle pour le cadre du texte

        if index_phrase < len(phrases):
            surface_texte.fill((0, 0, 0))  # Remplit la surface avec une couleur de fond noire
            lignes = []
            for i in range(index_phrase + 1):
                lignes.append(phrases[i])  # Ajoute les lignes de texte jusqu'à l'index_phrase actuel

            y_offset = 0
            for ligne in lignes:
                surface_ligne = police.render(ligne, True, (255, 165, 0))  # Rendu du texte avec la police et la couleur spécifiées
                surface_texte.blit(surface_ligne, (0, y_offset))  # Affiche la ligne de texte sur la surface_texte
                y_offset += surface_ligne.get_height()  # Ajuste l'offset vertical pour la ligne suivante

            index_phrase += 1

        time.sleep(vitesse_affichage)  # Pause pour contrôler la vitesse d'affichage

        screen.blit(surface_texte, (x, y))  # Affiche la surface_texte à l'écran

        pygame.display.flip()  # Mettre à jour l'affichage

        screen.fill((0,0,0))
        screen.blit(background, (0, 0))  # Affiche l'arrière-plan


    pygame.quit()  # Quitter Pygame à la fin de la boucle while

