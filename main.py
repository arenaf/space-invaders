import pygame

from bullet import Bullet
from ship import Ship

# Colours
# ship_bg = (154, 222, 123)
ship_bg = (95, 194, 50)
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
bullet = Bullet(300, 300)

# Imágenes
img_ship = pygame.image.load("assets/img/ship.png")
ship = Ship(screen_width//2, screen_height, img_ship, screen)
user_ship = ship.create_ship()

while run:
    clock.tick(fps)
    screen.fill((0, 0, 0))  # Refresca la ventana y pinta de negro

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Dibuja la nave
    ship.create_ship()
    # pygame.draw.rect(screen, ship_bg, user_ship)
    # Manejo de teclas
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        ship.move_right()
    if key[pygame.K_LEFT]:
        ship.move_left()
    if key[pygame.K_SPACE] and shot == False and (pygame.time.get_ticks() - last_shot > gun_cooldown):
        # b = Bullet(user_ship.x + user_ship.width//2, user_ship.y)
        b = Bullet(ship.rect.x + ship.rect.width // 2, ship.rect.y)
        shot = True
        last_shot = pygame.time.get_ticks()
        bullets.append(b)
    if key[pygame.K_SPACE] == False: # Si no está presionada la barra espaciadora, puede lanzar otro disparo
        shot = False

    # Disparos de la nave
    for b in bullets:
        pygame.draw.rect(screen, ship_bg, b)
        b.move_bullet()
        if b.rect.y < 0:
            bullets.remove(b)


    # Actualiza el lienzo para mostrar los cambios
    pygame.display.update()

pygame.quit()




