import pygame
from Play import *
import random
import time 
from tir import * 
# from test import partie_finie  
from finpartie import *
from checkcoule import *
from cristal import *



def affGrille(grille_pla, grille_tir_pla, niveau, dernier_tir_reussi, bateaux_ia, tirs_ia, pouvoir):
    pygame.init()

    # Définir les dimensions de la fenêtre
    largeur = 1050
    largeur_grille = 500
    hauteur = 750
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("Affichage de la Grille")

    # fond
    background = pygame.image.load("images/background_play.jpeg").convert()
    background = pygame.transform.scale(background, (largeur, hauteur))
    # screen.blit(background, (0, 0))

    # Couleurs
    # COULEUR_FOND = background
    COULEUR_GRILLE = (255, 165, 0)
    COULEUR_TEXTE = (255, 165, 0)
    ORANGE = (255, 165, 0)
    BLEU = (0, 0, 255)
    ROUGE = (255, 0, 0)
    GRIS = (128, 128, 128)
    VERT = (0, 255, 0)

    # Dimensions de la grille
    #Grille Tir: 265, 65
    nb_lignes_tir = 10
    nb_colonnes_tir = 10
    taille_case_tir = 310 // nb_colonnes_tir

    #Grille Bateau: 692, 110
    nb_lignes_bat = 10
    nb_colonnes_bat = 10
    taille_case_bat = 190 // nb_colonnes_bat

    # Initialiser les cases choisies
    cases_choisies = [[False] * 10 for _ in range(10)]

    # Variables pour afficher le message
    afficher_message_pla = 0
    debut_affichage_message_pla = 0 
    afficher_message_ia = 0
    debut_affichage_message_ia = 0 

    # Variable pour le décompte
    decompte = 0
    debut_decompte = time.time()

    # Pouvoir actif
    pouvoir_actif = False
    orientation_pouvoir = 'Horizontal'
    clairvoiance = False

    # Niveau
    niveau_cpt = 1

    # Fin de partie 
    fin_partie = 0
    result = ''

    # Boucle principale
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # print("Fermeture du jeu")
            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if clairvoiance:
                    pouvoir=''
                    pouvoir_actif= False
                
                pos = pygame.mouse.get_pos()
                colonne = (pos[0] - 265) // taille_case_tir
                ligne = (pos[1] - 65) // taille_case_tir

                if 0 <= ligne < nb_lignes_tir and 0 <= colonne < nb_colonnes_tir:
                    if grille_tir_pla[ligne][colonne] == -1:
                        print("Vous avez tiré en", ligne, colonne)
                        
                        if pouvoir == 'bombe' and pouvoir_actif == True:
                            pouvoir_actif = False
                            pouvoir = ''
                            voisins = [(ligne, colonne), (ligne - 1, colonne), (ligne + 1, colonne), (ligne, colonne - 1), (ligne, colonne + 1)]
                            for voisin_ligne, voisin_colonne in voisins:
                                if 0 <= voisin_ligne < nb_lignes_tir and 0 <= voisin_colonne < nb_colonnes_tir:
                                    if grille_pla[voisin_ligne][voisin_colonne] != -2:
                                        print(f"Dommages sur la case ({voisin_ligne}, {voisin_colonne})")
                                        if tir(voisin_ligne, voisin_colonne, bateaux_ia)==True:
                                            bateaux_ia[voisin_ligne][voisin_colonne] = -2  # Mettre à jour la grille de tir
                                            grille_tir_pla[voisin_ligne][voisin_colonne] = 1
                                        else :
                                            bateaux_ia[voisin_ligne][voisin_colonne] = -1
                                            grille_tir_pla[voisin_ligne][voisin_colonne] = 0
                        
                        elif pouvoir == 'rafale' and pouvoir_actif == True:
                                pouvoir_actif = False
                                pouvoir = ''

                                # Définir les coordonnées des cases voisines
                                if orientation_pouvoir == 'Horizontal':
                                    voisins = [(ligne, colonne), (ligne, colonne+1), (ligne, colonne+2)]
                                elif orientation_pouvoir == 'Vertical':
                                    voisins = [(ligne, colonne), (ligne+1, colonne), (ligne+2, colonne)]

                                for voisin_ligne, voisin_colonne in voisins:
                                    # Vérifier si les coordonnées du voisin sont valides
                                    if 0 <= voisin_ligne < nb_lignes_tir and 0 <= voisin_colonne < nb_colonnes_tir:
                                        # Vérifier si la case du voisin n'a pas déjà été touchée
                                        if grille_pla[voisin_ligne][voisin_colonne] != -2:
                                            print(f"Dommages sur la case ({voisin_ligne}, {voisin_colonne})")
                                            if tir(voisin_ligne, voisin_colonne, bateaux_ia):
                                                bateaux_ia[voisin_ligne][voisin_colonne] = -2  # Mettre à jour la grille de tir
                                                grille_tir_pla[voisin_ligne][voisin_colonne] = 1
                                            else:
                                                bateaux_ia[voisin_ligne][voisin_colonne] = -1
                                                grille_tir_pla[voisin_ligne][voisin_colonne] = 0 
                        
                        elif pouvoir == 'tempete' and pouvoir_actif == True:
                            pouvoir_actif = False
                            pouvoir = ''

                            # Déterminer les coordonnées des deuxième et troisième tirs
                            ligne2 = random.randint(0,9)
                            colonne2 = random.randint(0,9)
                            while grille_tir_pla[ligne2][colonne2] != -1:
                                ligne2 = random.randint(0,9)
                                colonne2 = random.randint(0,9)
                            ligne3 = random.randint(0,9)
                            colonne3 = random.randint(0,9)
                            while grille_tir_pla[ligne3][colonne3] != -1:
                                ligne3 = random.randint(0,9)
                                colonne3 = random.randint(0,9)

                            # Effectuer les deuxième et troisième tirs
                            if tir(ligne, colonne, bateaux_ia) == True:
                                # Mettre à jour la grille de tir
                                bateaux_ia[ligne][colonne] = -2
                                grille_tir_pla[ligne][colonne] = 1
                            else:
                                bateaux_ia[ligne][colonne] = -1
                                grille_tir_pla[ligne][colonne] = 0

                            if tir(ligne2, colonne2, bateaux_ia) == True:
                                # Mettre à jour la grille de tir
                                bateaux_ia[ligne2][colonne2] = -2
                                grille_tir_pla[ligne2][colonne2] = 1
                            else:
                                bateaux_ia[ligne2][colonne2] = -1
                                grille_tir_pla[ligne2][colonne2] = 0

                            if tir(ligne3, colonne3, bateaux_ia) == True:
                                # Mettre à jour la grille de tir
                                bateaux_ia[ligne3][colonne3] = -2
                                grille_tir_pla[ligne3][colonne3] = 1
                            else:
                                bateaux_ia[ligne3][colonne3] = -1
                                grille_tir_pla[ligne3][colonne3] = 0
                                    
                        elif tir(ligne, colonne, bateaux_ia)==True: 
                            
                            if pouvoir == 'missile' and pouvoir_actif == True:
                                tue = bateaux_ia[ligne][colonne]
                                for j, ligne in enumerate(bateaux_ia):
                                    for i, element in enumerate(ligne):
                                        if element == tue:
                                            grille_tir_pla[j][i] = 1 
                                            bateaux_ia[j][i] = -2
                                            afficher_message_pla = 3
                                            debut_affichage_message_pla = time.time()
                                pouvoir_actif = False
                                pouvoir = ''                                      


                            else: 
                                print("Touché !")
                                grille_tir_pla[ligne][colonne] = 1  # Mettre à jour la grille de tir

                                if checkcoule(bateaux_ia, bateaux_ia[ligne][colonne]):
                                    afficher_message_pla = 3
                                    debut_affichage_message_pla = time.time()
                                else:
                                    afficher_message_pla = 1
                                    debut_affichage_message_pla = time.time()

                                bateaux_ia[ligne][colonne] = -2
                                #Afficher "Touché !"



                        #Si c'est raté
                        else:                             
                            if pouvoir == 'missile' and pouvoir_actif == True:
                                pouvoir_actif = False
                                pouvoir = ''

                            print("Raté !")
                            grille_tir_pla[ligne][colonne] = 0  # Mettre à jour la grille de tir
                            bateaux_ia[ligne][colonne] = -1
                            afficher_message_pla = 2
                            debut_affichage_message_pla = time.time()
                        

                        #Tour de l'ordinateur
                        if niveau == 1:
                            ligne = random.randint(0,9)
                            colonne = random.randint(0,9)
                        elif niveau == 2:
                            print(f"dt{dernier_tir_reussi}")
                            if dernier_tir_reussi is not None:
                
                                new_var = tir_a_cote(dernier_tir_reussi, grille_pla)
                                ligne = new_var[0]
                                colonne = new_var[1]
                                print(f"ligne{new_var[0]}colonne{new_var[1]}")
                            else :
                                ligne = random.randint(0,9)
                                colonne = random.randint(0,9)
                        elif niveau == 3:
                            if niveau_cpt==3:
                                ligne, colonne = cristal(grille_pla)
                                niveau_cpt=1
                            else:
                                print(f"dt{dernier_tir_reussi}")
                                if dernier_tir_reussi is not None:
                    
                                    new_var = tir_a_cote(dernier_tir_reussi, grille_pla)
                                    ligne = new_var[0]
                                    colonne = new_var[1]
                                    print(f"ligne{new_var[0]}colonne{new_var[1]}")
                                else :
                                    ligne = random.randint(0,9)
                                    colonne = random.randint(0,9)
                                niveau_cpt = niveau_cpt + 1
                        while tirs_ia[ligne][colonne] != -1:
                            ligne = random.randint(0,9)
                            colonne = random.randint(0,9)
                        print(f"ligne{ligne}colonne{colonne}")
                        if tir(ligne, colonne, grille_pla)==True: 
                            print("L'ordinateur vous à touché !")
                            grille_pla[ligne][colonne] = -2  # Mettre à jour la grille de tir
                            tirs_ia[ligne][colonne] = 1
                            afficher_message_ia = 1
                            debut_affichage_message_pla = time.time()
                            dernier_tir_reussi = (ligne, colonne)

                        else:
                            print("L'ordinateur vous à raté !")
                            grille_pla[ligne][colonne] = -1  # Mettre à jour la grille de tir
                            tirs_ia[ligne][colonne] = 0
                            afficher_message_ia = 2
                            debut_affichage_message_pla = time.time()
                            dernier_tir_reussi = None



                        


                    else:
                        print("Vous avez déjà tiré en", ligne, colonne, ", choisissez une autre case")


                if finpartie(grille_pla, bateaux_ia)=='Défaite' or finpartie(grille_pla, bateaux_ia)=='Victoire':
                    #running = False
                    result = finpartie(grille_pla, bateaux_ia)
                    fin_partie = 1

                    print("Partie finie !")
                else: 
                    print("pas fini")

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p and pouvoir != '':
                    pouvoir_actif = True
                    if pouvoir=='clairvoyance':
                        xx, yy = cristal(bateaux_ia)
                        print(xx, yy)
                        bateaux_ia[xx][yy] = 10
                        grille_tir_pla[xx][yy] = 10   
                        clairvoiance = True
                        
             
                if event.key == pygame.K_v and pouvoir == 'triplette maudite' and pouvoir_actif == True:
                    orientation_pouvoir = 'Vertical'
                if event.key == pygame.K_h and pouvoir == 'triplette maudite' and pouvoir_actif == True:
                    orientation_pouvoir = 'Horizontal'
                
                        

        police = pygame.font.Font(None, 21)
        police_pouv = pygame.font.Font(None, 20)
        police_message = pygame.font.Font(None, 50)
        police_fin = pygame.font.Font(None, 60)


        # Effacer l'écran
        # fenetre.fill(COULEUR_FOND)
        fenetre.fill((0, 0, 0))
        fenetre.blit(background, (0, 0))

        if fin_partie == 0:
        
            # Dessiner la grille bateau
            for ligne in range(nb_lignes_bat):
                for colonne in range(nb_colonnes_bat):
                    x = colonne * taille_case_bat + 692
                    y = ligne * taille_case_bat + 110

                    if 1<=grille_pla[ligne][colonne]<=5:
                        # pygame.draw.rect(fenetre, ORANGE, (x, y, taille_case_bat, taille_case_bat))
                        pygame.draw.rect(fenetre, VERT, (x, y, taille_case_bat, taille_case_bat))
                    elif grille_pla[ligne][colonne] == 0:
                        pygame.draw.rect(fenetre, COULEUR_GRILLE, (x, y, taille_case_bat, taille_case_bat), 1)
                    elif grille_pla[ligne][colonne] == -1:
                        pygame.draw.rect(fenetre, GRIS, (x, y, taille_case_bat, taille_case_bat))
                    elif grille_pla[ligne][colonne] == -2:
                        pygame.draw.rect(fenetre, ROUGE, (x, y, taille_case_bat, taille_case_bat))

                    


            # Dessiner la grille de tirs
            for ligne in range(nb_lignes_tir):
                for colonne in range(nb_colonnes_tir):
                    x = colonne * taille_case_tir + 265
                    y = ligne * taille_case_tir + 65

                    if grille_tir_pla[ligne][colonne]==1:
                        # pygame.draw.rect(fenetre, ORANGE, (x, y, taille_case_tir, taille_case_tir))
                        pygame.draw.rect(fenetre, VERT, (x, y, taille_case_tir, taille_case_tir))
                        cases_choisies[ligne][colonne] = True
                    elif grille_tir_pla[ligne][colonne] == -1:
                        pygame.draw.rect(fenetre, COULEUR_GRILLE, (x, y, taille_case_tir, taille_case_tir), 1)
                    elif grille_tir_pla[ligne][colonne] == 0:
                        pygame.draw.rect(fenetre, GRIS, (x, y, taille_case_tir, taille_case_tir))
                        cases_choisies[ligne][colonne] = True
                    elif grille_tir_pla[ligne][colonne] == 10:
                        pygame.draw.rect(fenetre, BLEU, (x, y, taille_case_tir, taille_case_tir))




            # Afficher le texte d'information
            info_texte = "Vous tirez à gauche"
            texte_info = police.render(info_texte, True, (255, 165, 0))
            fenetre.blit(texte_info, (10, 70))

            # Afficher le texte d'information
            info_texte = "Votre grille est à droite"
            texte_info = police.render(info_texte, True, (255, 165, 0))
            fenetre.blit(texte_info, (10, 90))

            # Afficher le texte d'information
            info_texte = "L'IA tirera après vous"
            texte_info = police.render(info_texte, True, (255, 165, 0))
            fenetre.blit(texte_info, (10, 110))

            # Touché / coulé joueur 
            if afficher_message_pla==1:
                message_texte = "TOUCHÉ"
                texte_message = police_message.render(message_texte, True, (255, 165, 0))
                texte_rect = texte_message.get_rect(center=(538, 573))
                fenetre.blit(texte_message, texte_rect)
                # fenetre.blit(texte_message, (500, 570))

                # Vérifier si le temps d'affichage du message est écoulé
                if time.time() - debut_affichage_message_pla > 1:
                    afficher_message_pla = 0
            elif afficher_message_pla==2:
                message_texte = "RATÉ"
                texte_message = police_message.render(message_texte, True, (255, 165, 0))
                texte_rect = texte_message.get_rect(center=(538, 573))
                fenetre.blit(texte_message, texte_rect)
                # fenetre.blit(texte_message, (500, 570))

                # Vérifier si le temps d'affichage du message est écoulé
                if time.time() - debut_affichage_message_pla > 1:
                    afficher_message_pla = 0
            elif afficher_message_pla==3:
                message_texte = "COULÉ"
                texte_message = police_message.render(message_texte, True, (255, 165, 0))
                texte_rect = texte_message.get_rect(center=(538, 573))
                fenetre.blit(texte_message, texte_rect)
                # fenetre.blit(texte_message, (320, 430))

                # Vérifier si le temps d'affichage du message est écoulé
                if time.time() - debut_affichage_message_pla > 1:
                    afficher_message_pla = 0

            # Touché / coulé IA 
            if afficher_message_ia==1:
                message_texte = "L'IA vous a touché"
                texte_message = police_pouv.render(message_texte, True, (255, 165, 0))
                fenetre.blit(texte_message, (710, 438))
                # Vérifier si le temps d'affichage du message est écoulé
                if time.time() - debut_affichage_message_pla > 1:
                    afficher_message_ia = 0
            elif afficher_message_ia==2:
                message_texte = "L'IA vous a raté"
                texte_message = police_pouv.render(message_texte, True, (255, 165, 0))
                fenetre.blit(texte_message, (710, 438))
                # Vérifier si le temps d'affichage du message est écoulé
                if time.time() - debut_affichage_message_pla > 1:
                    afficher_message_ia = 0            



            # Activation pouvoir 
            if pouvoir_actif == True:
                info_texte = f"Pouvoir actif : {pouvoir}"
                texte_info = police_pouv.render(info_texte, True, (255, 165, 0))
                fenetre.blit(texte_info, (263, 430))

            # Activer pouvoir  
            info_texte = "Activer pouvoir : 'p'"
            texte_info = police.render(info_texte, True, (255, 165, 0))
            fenetre.blit(texte_info, (10, 130)) 

            # Afficher niveau
            info_texte = f"Niveau : {niveau}"
            texte_info = police.render(info_texte, True, (255, 165, 0))
            fenetre.blit(texte_info, (10, 150))

            # Rafale 
            if pouvoir == 'rafale':
                info_texte = f"Rafale: Tirez sur trois"
                texte_info = police.render(info_texte, True, (255, 165, 0))
                fenetre.blit(texte_info, (10, 190)) 
                info_texte = f"cases voisines"
                texte_info = police.render(info_texte, True, (255, 165, 0))
                fenetre.blit(texte_info, (10, 210)) 
                info_texte = f"Orientation : {orientation_pouvoir}"
                texte_info = police.render(info_texte, True, (255, 165, 0))
                fenetre.blit(texte_info, (9, 230)) 

            # Bombe 
            if pouvoir == 'bombe':
                info_texte = "Bombe: Tirez sur les"
                texte_info = police.render(info_texte, True, (255, 165, 0))
                fenetre.blit(texte_info, (10, 190)) 
                info_texte = "quatres cases voisines"
                texte_info = police.render(info_texte, True, (255, 165, 0))
                fenetre.blit(texte_info, (10, 210)) 
                info_texte = "de votre cible"
                texte_info = police.render(info_texte, True, (255, 165, 0))
                fenetre.blit(texte_info, (10, 230)) 

            # Tempete 
            if pouvoir == 'tempete':
                info_texte = "Tempete: Tirez sur"
                texte_info = police.render(info_texte, True, (255, 165, 0))
                fenetre.blit(texte_info, (10, 190))    
                info_texte = "deux autres cases"
                texte_info = police.render(info_texte, True, (255, 165, 0))
                fenetre.blit(texte_info, (10, 210)) 
                info_texte = "aléatoirement"
                texte_info = police.render(info_texte, True, (255, 165, 0))
                fenetre.blit(texte_info, (10, 230)) 

            # Missile 
            if pouvoir == 'missile':
                info_texte = "Missile: Coulez un"
                texte_info = police.render(info_texte, True, (255, 165, 0))
                fenetre.blit(texte_info, (10, 190))        
                info_texte = "bateau en un tir"  
                texte_info = police.render(info_texte, True, (255, 165, 0))
                fenetre.blit(texte_info, (10, 210)) 

            # Clairvoyance 
            if pouvoir == 'clairvoyance':
                info_texte = "Clairvoyance: découvrez"
                texte_info = police.render(info_texte, True, (255, 165, 0))
                fenetre.blit(texte_info, (10, 190)) 
                info_texte = "case aléatoirement"
                texte_info = police.render(info_texte, True, (255, 165, 0))
                fenetre.blit(texte_info, (10, 210)) 

        elif fin_partie == 1:
            if result=='Victoire':
                info_texte = "Vous avez gagné"
            elif result=='Défaite':
                info_texte = "Vous avez perdu"
            texte_result = police_fin.render(info_texte, True, (255, 165, 0))
            texte_res_rect = texte_result.get_rect(center=(420, 220))
            fenetre.blit(texte_result, texte_res_rect)       




        # Mettre à jour l'affichage
        pygame.display.flip()




    # Quitter Pygame
    pygame.quit()

def tir_a_cote(coord_dernier_tir, grille_pla):
    ligne, colonne = coord_dernier_tir
    voisins = [(ligne-1, colonne), (ligne+1, colonne), (ligne, colonne-1), (ligne, colonne+1)]
    valide_voisins = []
    
    for voisin in voisins:
        v_ligne, v_colonne = voisin
        if 0 <= v_ligne < 10 and 0 <= v_colonne < 10 :
            valide_voisins.append(voisin)
            new_cible = random.choice(valide_voisins)       
    if valide_voisins:
        return new_cible
    else:
        # Si aucun voisin valide n'est trouvé, retourner des coordonnées aléatoires
        return (random.randint(0, 9),random.randint(0, 9))

