import pygame
import sys

# Initialiser Pygame
pygame.init()

COLOR = (255, 255, 0)
# Définir les dimensions de la fenêtre
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animation de marche")
screen.fill(COLOR)

# Charger les images du personnage
droite1 = pygame.image.load("img_perso/droite1-removebg-preview.png")
droite2 = pygame.image.load("img_perso/droite2-removebg-preview.png")
droite3 = pygame.image.load("img_perso/droite3-removebg-preview.png")

gauche1 = pygame.image.load("img_perso/gauche1-removebg-preview.png")
gauche2 = pygame.image.load("img_perso/gauche2-removebg-preview.png")
gauche3 = pygame.image.load("img_perso/gauche3-removebg-preview.png")

haut1 = pygame.image.load("img_perso/derriere1-removebg-preview.png")
haut2 = pygame.image.load("img_perso/derriere2-removebg-preview.png")
haut3 = pygame.image.load("img_perso/derriere3-removebg-preview.png")

bas1 = pygame.image.load("img_perso/devant1-removebg-preview.png")
bas2 = pygame.image.load("img_perso/devant2-removebg-preview.png")
bas3 = pygame.image.load("img_perso/devant3-removebg-preview.png")

# Créer des listes d'images pour chaque direction
images_droite = [droite1, droite2, droite3]
images_gauche = [gauche1, gauche2, gauche3]
images_haut = [haut1, haut2, haut3]
images_bas = [bas1, bas2, bas3]

# Définir les variables initiales
x, y = 50, screen_height // 2
velocity = 25
current_image = 0
clock = pygame.time.Clock()
direction = "droite"

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Mettre à jour la direction et la position du personnage
    if keys[pygame.K_RIGHT]:
        x += velocity
        direction = "droite"
        current_image = (current_image + 1) % 3
    elif keys[pygame.K_LEFT]:
        x -= velocity
        direction = "gauche"
        current_image = (current_image + 1) % 3
    elif keys[pygame.K_UP]:
        y -= velocity
        direction = "haut"
        current_image = (current_image + 1) % 3
    elif keys[pygame.K_DOWN]:
        y += velocity
        direction = "bas"
        current_image = (current_image + 1) % 3

    # Remplir l'écran de jaune
    screen.fill(COLOR)

    # Dessiner l'image actuelle du personnage en fonction de la direction
    if direction == "droite":
        screen.blit(images_droite[current_image], (x, y))
    elif direction == "gauche":
        screen.blit(images_gauche[current_image], (x, y))
    elif direction == "haut":
        screen.blit(images_haut[current_image], (x, y))
    elif direction == "bas":
        screen.blit(images_bas[current_image], (x, y))

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Réguler la vitesse de l'animation
    clock.tick(20)

pygame.quit()
sys.exit()
