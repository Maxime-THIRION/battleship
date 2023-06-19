import pygame

screen = pygame.display.set_mode((1000, 700))  # Création de la fenêtre graphique

def display_title(texte):
    font = pygame.font.Font("bebas_neue/BebasNeue-Regular.ttf", 90)  # Définition de la police et de la taille du texte
    surface_texte = font.render(texte, True, (255, 255, 255))  # Génération de la surface de texte
    rect = surface_texte.get_rect()  # Obtention du rectangle entourant le texte
    rect.center = (screen.get_width() // 2, screen.get_height() // 2)  # Centrage du rectangle dans la fenêtre
    screen.blit(surface_texte, rect)  # Affichage du texte centré sur l'écran

def display_text(texte, police, taille, x, y, c1, c2, c3):
    font = pygame.font.Font(police, taille)  # Définition de la police et de la taille du texte
    surface_texte = font.render(texte, True, (c1, c2, c3))  # Génération de la surface de texte
    screen.blit(surface_texte, (x, y))  # Affichage de la surface de texte à la position (x, y)

def split_phrases(texte):
    phrases = texte.split('. ')  # Découpage du texte en phrases individuelles en utilisant '. ' comme séparateur
    return phrases
