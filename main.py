import pygame

from bullet import Bullet
from ship import Ship

# Colours
ship_bg = (154, 222, 123)

# fps
fps = 60

# Inicializa la ventana
pygame.init()

# Tamaño de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

ship = Ship(screen_width//2, screen_height)
user_ship = ship.create_ship()

shots = []
run = True
bullet = Bullet(300, 300)
clock = pygame.time.Clock()

while run:
    clock.tick(fps)
    screen.fill((0, 0, 0))  # Refresca la ventana y pinta de negro

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Dibuja la nave
    pygame.draw.rect(screen, ship_bg, user_ship)

    # Manejo de teclas
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        ship.move_right(user_ship)
    if key[pygame.K_LEFT]:
        ship.move_left(user_ship)
    if key[pygame.K_UP]:
        bullet = Bullet(user_ship.x, user_ship.y-20)
        pygame.draw.rect(screen, ship_bg, bullet)
        # bullet.update()
        # bullet = Bullet(user_ship.rect.centerx, user_ship.rect.centery)
        # pygame.draw.rect(screen, ship_bg, ship.attack(user_ship))
    # bullet = Bullet(user_ship.x, user_ship.y - 20)
    pygame.draw.rect(screen, ship_bg, bullet)
    bullet.move()
    # time.tick(30)
    # Actualiza el lienzo para mostrar los cambios
    pygame.display.update()

pygame.quit()




