# Importation des modules requis
import pygame
import sys

# Initialiser
pygame.init()

# Configuration de la fenêtre de l'écran d'accueil
screen = pygame.display.set_mode((400, 400))

# Définir le titre de la fenêtre(le nom de jeu)
pygame.display.set_caption('My first game')
# Remplir la couleur de fond de la fenêtre
screen.fill((156, 156, 156))
# Introduction des types de polices
f = pygame.font.SysFont('Arial', 50)
# Génère un message texte
"""
Paramètre:
1.Le contenu du texte
2.La police est lisse ou non
3.La couleur de la police en RGB(red green blue)
4.La couleur de fond de la police en RGB(red green blue)
"""
text = f.render('Happy game', True, (135, 206, 235), (240, 255, 255))

# Obtenir les coordonnées de la zone rectangulaire de l'objet affiché
textRect = text.get_rect()

# Définir l'objet d'affichage pour qu'il soit centré
textRect.center = (200, 200)

# Prenez le message texte préparé et dessinez-le sur l'écran d'accueil
screen.blit(text, textRect)


while True:
    # Boucle pour les événements et écoute pour le statut de l'événement
    for event in pygame.event.get():
        # Déterminer si l'utilisateur a cliqué sur le bouton de fermeture 'x'
        if event.type == pygame.QUIT:
            # Désinstaller tous les modules
            pygame.quit()
            # Terminer la procédure et assurer la sortie
            sys.exit()
    pygame.display.flip()   # Mise à jour du contenu de l'écran