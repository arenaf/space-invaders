import random
import pygame
from alien import Alien
from bullet import Bullet
from ship import Ship

# Colours
# ship_bg = (154, 222, 123)
ship_bg = (154, 222, 123)
bullet_bg = (154, 222, 123)
# bullet_alien_bg = (199, 128, 250)
bullet_alien_bg = (253, 253, 189)
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
shot_alien = False
last_shot_alien = 0
run = True
bullets = pygame.sprite.Group()
alien_bullets_list = pygame.sprite.Group()
clock = pygame.time.Clock()
y = 100
x = 100


# Imágenes
img_ship = pygame.image.load("assets/img/ship.png")
img_crab = pygame.image.load("assets/img/crab.png")
img_octopus = pygame.image.load("assets/img/octopus.png")
img_squid = pygame.image.load("assets/img/squid.png")


# Crea los objetos

ship = Ship(screen_width//2, screen_height, img_ship, screen)
ship2 = Ship(30, 75, img_ship, screen)
ship3 = Ship(80, 75, img_ship, screen)

ship_list = []
ship_list.append(ship)
ship_list.append(ship2)
ship_list.append(ship3)


crab = Alien(x, y, img_crab, screen)
pos_crabs = crab.create_aliens(1, 11)

octopus = Alien(x, y+50, img_octopus, screen)
pos_octopus = octopus.create_aliens(2, 11)

squid = Alien(x, y+150, img_squid, screen)
pos_squid = squid.create_aliens(2, 11)
# all_aliens = []
all_aliens = pygame.sprite.Group()
# Dibuja los aliens
# all_crabs = []
for i in pos_crabs:
    # crab = Alien(i[0], i[1], img_crab, screen)
    crab = Alien(i[0], i[1], img_crab, screen)
    # all_crabs.append(crab)
    all_aliens.add(crab)

# all_octopus = []
for i in pos_octopus:
    octopus = Alien(i[0], i[1], img_octopus, screen)
    # all_octopus.append(octopus)
    all_aliens.add(octopus)

# all_squid = []
for i in pos_squid:
    squid = Alien(i[0], i[1], img_squid, screen)
    # all_squid.append(squid)
    all_aliens.add(squid)



while run:
    clock.tick(fps)
    screen.fill((0, 0, 0))  # Refresca la ventana y pinta de negro

    pygame.draw.line(screen, (199, 128, 250), (0, 50), (screen_width, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Dibuja las naves
    ship.create_ship()
    ship2.create_ship()
    ship3.create_ship()

    # Dibuja los aliens
    all_aliens.draw(screen)

    # Mueve los aliens
    all_aliens.update(all_aliens)

    # Disparos de los aliens
    if (shot_alien == False and
            (pygame.time.get_ticks() - last_shot_alien > gun_cooldown) and
            (len(alien_bullets_list) < 2)):
        bullet_alien = random.choice(all_aliens.sprites())
        b_allien = Bullet(bullet_alien.rect.x, bullet_alien.rect.y)
        shot_alien = True
        last_shot_alien = pygame.time.get_ticks()
        alien_bullets_list.add(b_allien)

    if len(alien_bullets_list) < 2:
        shot_alien = False
    for ba in alien_bullets_list:
        pygame.draw.rect(screen, bullet_alien_bg, ba)
        ba.move_bullet_alien()
        if ba.rect.y > screen_height:
            ba.kill()


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
        bullets.add(b)
    if key[pygame.K_SPACE] == False: # Si no está presionada la barra espaciadora, puede lanzar otro disparo
        shot = False
    for b in bullets:
        pygame.draw.rect(screen, bullet_bg, b)
        b.move_bullet()
        if b.rect.y < 0:
            b.kill()
            # bullets.remove(b)

    # Colisión
    if pygame.sprite.spritecollide(ship, alien_bullets_list, dokill=False):
        print("Colisión contra nave")


    for bullet in bullets:
        collision_alien = pygame.sprite.spritecollide(bullet, all_aliens, True)
        if collision_alien != []:
            bullet.kill()


    # Actualiza el lienzo para mostrar los cambios
    # pygame.display.update()
    pygame.display.flip()

pygame.quit()
