import pygame

from alien import Alien
from bullet import Bullet
from ship import Ship

# Colours
# ship_bg = (154, 222, 123)
ship_bg = (154, 222, 123)
# fps
fps = 60

# Inicializa la ventana
pygame.init()

# Tamaño de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")



# Variables
shot = False # Controla si el arma está disparada
gun_cooldown = 500
last_shot = 0
run = True
bullets = []
clock = pygame.time.Clock()
# bullet = Bullet(300, 300)

# Imágenes
img_ship = pygame.image.load("assets/img/ship.png")
img_crab = pygame.image.load("assets/img/crab.png")
img_octopus = pygame.image.load("assets/img/octopus.png")
img_squid = pygame.image.load("assets/img/squid.png")


ship = Ship(screen_width//2, screen_height, img_ship, screen)
crab = Alien(200, 50, img_crab, screen)
octopus = Alien(200, 150, img_octopus, screen)
squid = Alien(200, 250, img_squid, screen)


while run:
    clock.tick(fps)
    screen.fill((0, 0, 0))  # Refresca la ventana y pinta de negro

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Dibuja la nave
    ship.create_ship()

    # Dibuja los aliens
    crab.draw_alien()
    octopus.draw_alien()
    squid.draw_alien()

    # Manejo de teclas
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        ship.move_right()
    if key[pygame.K_LEFT]:
        ship.move_left()

    # Disparos de la nave
    if key[pygame.K_SPACE] and shot == False and (pygame.time.get_ticks() - last_shot > gun_cooldown):
        b = Bullet(ship.rect.x + ship.rect.width // 2, ship.rect.y)
        shot = True
        last_shot = pygame.time.get_ticks()
        bullets.append(b)
    if key[pygame.K_SPACE] == False: # Si no está presionada la barra espaciadora, puede lanzar otro disparo
        shot = False
    for b in bullets:
        pygame.draw.rect(screen, ship_bg, b)
        b.move_bullet()
        if b.rect.y < 0:
            bullets.remove(b)

    # Actualiza el lienzo para mostrar los cambios
    pygame.display.update()

pygame.quit()
