import pygame
from Function import *  

couleur_bouton = (255, 255, 255)  # Couleur du bouton (blanc dans cet exemple)
couleur_texte = (0, 0, 0)  # Couleur du texte du bouton (noir dans cet exemple)

def draw_rounded_rect(surface, couleur, rect, radius):
    pygame.draw.rect(surface, couleur, rect, border_radius=radius)  # Dessine un rectangle arrondi sur la surface
    corners = [(rect.left + radius, rect.top + radius),
               (rect.right - radius, rect.top + radius),
               (rect.left + radius, rect.bottom - radius),
               (rect.right - radius, rect.bottom - radius)]
    for corner in corners:
        pygame.draw.circle(surface, couleur, corner, radius)  # Dessine un cercle aux coins du rectangle pour arrondir les angles

class Bouton:
    def __init__(self, x, y, largeur, hauteur, texte):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.texte = texte

    def display(self):
        rect = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)  # Crée un rectangle pour le bouton
        draw_rounded_rect(screen, couleur_bouton, rect, 5)  # Dessine le bouton arrondi sur la surface

        font = pygame.font.Font("bebas_neue/BebasNeue-Regular.ttf", 25)  # Définit la police et la taille du texte
        texte_surface = font.render(self.texte, True, couleur_texte)  # Génère la surface du texte
        texte_rect = texte_surface.get_rect(center=(self.x + self.largeur / 2, self.y + self.hauteur / 2))  # Obtient le rectangle du texte centré
        screen.blit(texte_surface, texte_rect)  # Affiche le texte sur la surface

    def check_clic(self, position):
        if self.x < position[0] < self.x + self.largeur and self.y < position[1] < self.y + self.hauteur:
            return True  # Retourne True si les coordonnées de la position sont à l'intérieur du bouton
        else:
            return False  # Retourne False sinon