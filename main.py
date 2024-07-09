import random
import pygame
from alien import Alien
from bullet import Bullet
from score import Score
from ship import Ship

# Colours
# ship_bg = (154, 222, 123)
ship_bg = (154, 222, 123)
bullet_bg = (154, 222, 123)
bullet_alien_bg = (199, 128, 250)
text_color = (180, 180, 184)
game_over_color = (227, 225, 217)
# bullet_alien_bg = (253, 253, 189)
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

score = Score()

speed = 1
# posiciones alienígenas
def create_positions(row, col):
    aliens_list = []
    new_y = y
    for i in range(row):
        new_x = x
        for j in range(col):
            aliens_list.append((new_x, new_y))
            new_x += 50
        new_y += 50
    return aliens_list

all_aliens = pygame.sprite.Group()
def create_aliens(speed):
    alien_positions = create_positions(5, 11)
    for i in alien_positions:
        if i[1] == x:
            crab = Alien(i[0], i[1], img_crab, speed)
            all_aliens.add(crab)
        if i[1] == x+50 or i[1] == x+100:
            octopus = Alien(i[0], i[1], img_octopus, speed)
            all_aliens.add(octopus)
        if i[1] == x+150 or i[1] == x+200:
            squid = Alien(i[0], i[1], img_squid, speed)
            all_aliens.add(squid)

create_aliens(speed)


# Textos
text = pygame.font.Font(None, 25)
font_game_over = pygame.font.Font(None, 75)
game_over_text = font_game_over.render("GAME OVER", True, game_over_color)

while run:
    clock.tick(fps)
    if len(ship_list) > 0:
        screen.fill((0, 0, 0))  # Refresca la ventana y pinta de negro
        pygame.draw.line(screen, (249, 245, 246), (0, 50), (screen_width, 50))
        score_text = text.render(f"Score: {score.score}", 0, text_color)
        screen.blit(score_text, (700, 10))
        level_text = text.render(f"Level:  {score.level}", 0, text_color)
        screen.blit(level_text, (700, 30))




        # Dibuja las naves
        for new_ship in ship_list:
            new_ship.create_ship()

        # Dibuja los aliens
        all_aliens.draw(screen)

        # Mueve los aliens
        all_aliens.update(all_aliens)

        # Sube de fase si no hay más aliens


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
    # if pygame.sprite.spritecollide(ship, alien_bullets_list, dokill=False):
    #     print("Colisión contra nave")
    # Colisiones a la nave
    for bul in alien_bullets_list:
        if ship.rect.colliderect(bul.rect):
            bul.kill()
            if len(ship_list) > 0:
                ship_list.pop(len(ship_list)-1)
            if len(ship_list) == 0:
                print("GAME OVER")
                screen.fill((211, 118, 118))
                text_rect = game_over_text.get_rect(center=(screen_width//2, screen_height//2))
                screen.blit(game_over_text, text_rect)

    # Colisiones a los alien
    for bullet in bullets:
        collision_alien = pygame.sprite.spritecollide(bullet, all_aliens, True)
        if collision_alien != []:
            score.new_score()
            bullet.kill()
        if len(all_aliens) == 0:
            score.new_level()
            speed += 1
            create_aliens(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Actualiza el lienzo para mostrar los cambios
    # pygame.display.update()
    pygame.display.flip()

    if len(ship_list) == 0:
        print("GAME OVER")
        screen.fill((211, 118, 118))
        text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(game_over_text, text_rect)


pygame.quit()
