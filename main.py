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

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Dibuja la nave
    pygame.draw.rect(screen, ship_bg, ship.create_ship())
    # Actualiza el lienzo para mostrar los cambios
    pygame.display.update()

pygame.quit()




