import pygame
from ship import Ship

# Colours
ship_bg = (154, 222, 123)

ship = Ship()

# Inicializa la ventana
pygame.init()

# Tamaño de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

user_ship = ship.create_ship()

shots = []
run = True

while run:

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
        new_shot = pygame.draw.rect(screen, ship_bg, ship.attack(user_ship))
        shots.append(new_shot)
    for shot in shots:
        shot.move_ip(0, -1)

    # Actualiza el lienzo para mostrar los cambios
    pygame.display.update()

pygame.quit()




