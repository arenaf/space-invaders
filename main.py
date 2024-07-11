import random
import pygame
from alien import Alien
from bullet import Bullet
from explosion import Explosion
from score import Score
from ship import Ship
import constants

# Inicializa la ventana
pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Temporizador
clock = pygame.time.Clock()

# Variables
shot = False  # Controla si el arma está disparada
last_shot = 0
shot_alien = False
last_shot_alien = 0
final_explosion = 0
y = 100
x = 100
speed = constants.SPEED_INCREASE
count = 3
last_count = pygame.time.get_ticks()
run = True
show_init_screen = True

# Grupos de sprites
bullets = pygame.sprite.Group()
alien_bullets_list = pygame.sprite.Group()
all_aliens = pygame.sprite.Group()
explotion_img = pygame.sprite.Group()

# Imágenes
img_ship = pygame.image.load("assets/img/ship.png")
img_crab = pygame.image.load("assets/img/crab.png")
img_octopus = pygame.image.load("assets/img/octopus.png")
img_squid = pygame.image.load("assets/img/squid.png")
start_img = pygame.image.load("assets/img/start.png")
restart_img = pygame.image.load("assets/img/restart.png")
exit_img = pygame.image.load("assets/img/exit.png")
bg = pygame.image.load("assets/img/bg.png")

# Crea los objetos
ship = Ship(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT, img_ship, screen)
ship2 = Ship(30, 75, img_ship, screen)
ship3 = Ship(80, 75, img_ship, screen)

score = Score()

def init_screen():
    screen.blit(bg, (0, 0))
    # Botón start
    start_button.center = (constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2)
    screen.blit(start_img, start_button)
    pygame.display.update()

# Crea las posiciones alienígenas
def create_alien_positions(row, col):
    aliens_list = []
    new_y = y
    for i in range(row):
        new_x = x
        for j in range(col):
            aliens_list.append((new_x, new_y))
            new_x += 50
        new_y += 50
    return aliens_list


# Crea los aliens
def create_aliens(speed):
    alien_positions = create_alien_positions(5, 11)
    for i in alien_positions:
        if i[1] == x:
            crab = Alien(i[0], i[1], img_crab, speed)
            all_aliens.add(crab)
        if i[1] == x + 50 or i[1] == x + 100:
            octopus = Alien(i[0], i[1], img_octopus, speed)
            all_aliens.add(octopus)
        if i[1] == x + 150 or i[1] == x + 200:
            squid = Alien(i[0], i[1], img_squid, speed)
            all_aliens.add(squid)


# Crea una lista con 3 naves que serán las vidas del jugador
def create_ship_list():
    list_all_ships = []
    list_all_ships.append(ship)
    list_all_ships.append(ship2)
    list_all_ships.append(ship3)
    return list_all_ships


# Textos
def create_texts():
    pygame.draw.line(screen, constants.TEXT_COLOR, (0, 50), (constants.SCREEN_WIDTH, 50))
    score_text = font_score.render(f"Score: {score.score}", 0, constants.TEXT_COLOR)
    screen.blit(score_text, constants.SCORE_TEXT_POSITION)
    level_text = font_score.render(f"Level: {score.level}", 0, constants.TEXT_COLOR)
    screen.blit(level_text, constants.LEVEL_TEXT_POSITION)
    high_score_text = font_high_score.render(f"Highest Score: {score.high_score}", 0, constants.TEXT_COLOR)
    screen.blit(high_score_text, constants.HIGH_SCORE_TEXT_POSITION)

# Fuentes y tamaño de los textos
font_score = pygame.font.Font(None, constants.FONT_SCORE_SIZE)
font_high_score = pygame.font.Font(None, constants.FONT_HIGH_SCORE_SIZE)
font_game_over = pygame.font.Font(None, constants.FONT_GAME_OVER_SIZE)
game_over_text = font_game_over.render("GAME OVER", True, constants.GAME_OVER_COLOR)


create_aliens(speed)
ship_list = create_ship_list()
start_button = start_img.get_rect()

while run:

    if show_init_screen:
        init_screen()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    show_init_screen = False
            if event.type == pygame.QUIT:
                run = False

    if show_init_screen == False:
        clock.tick(constants.FPS)
        if len(ship_list) > 0:
            # screen.blit(bg, (0, 0))
            screen.fill(constants.INIT_SCREEN_BG)  # Refresca la ventana y pinta de negro
            create_texts()
            # Funciones draw
            for new_ship in ship_list:
                new_ship.create_ship()

        all_aliens.draw(screen)
        explotion_img.draw(screen)

        # Funciones update
        all_aliens.update(all_aliens)
        explotion_img.update()

        # Disparos de los aliens
        if (shot_alien == False and
                (pygame.time.get_ticks() - last_shot_alien > constants.GUN_COOLDOWN) and
                (len(alien_bullets_list) < 3)):
            bullet_alien = random.choice(all_aliens.sprites())
            b_allien = Bullet(bullet_alien.rect.x, bullet_alien.rect.y)
            last_shot_alien = pygame.time.get_ticks()
            alien_bullets_list.add(b_allien)
            shot_alien = True

        if len(alien_bullets_list) < 3:
            shot_alien = False

        for ba in alien_bullets_list:
            pygame.draw.rect(screen, constants.BULLET_ALIEN_BG, ba)
            ba.move_bullet_alien()
            if ba.rect.y > constants.SCREEN_HEIGHT:
                ba.kill()

        # Manejo de teclas
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            ship.move_right()
        if key[pygame.K_LEFT]:
            ship.move_left()

        # Disparos de la nave
        if key[pygame.K_SPACE] and shot == False and (pygame.time.get_ticks() - last_shot > constants.GUN_COOLDOWN):
            b = Bullet(ship.rect.x + ship.rect.width // 2, ship.rect.y)
            last_shot = pygame.time.get_ticks()
            bullets.add(b)
            shot = True

        if key[pygame.K_SPACE] == False:  # Si no está presionada la barra espaciadora, puede lanzar otro disparo
            shot = False

        for b in bullets:
            pygame.draw.rect(screen, constants.BULLET_BG, b)
            b.move_bullet()
            if b.rect.y < 0:
                b.kill()

        # Colisiones
        # Colisión con la nave
        for bul in alien_bullets_list:
            if ship.rect.colliderect(bul.rect):
                explotion = Explosion(ship.rect.centerx, ship.rect.centery)
                explotion_img.add(explotion)
                bul.kill()

                if len(ship_list) > 0:
                    ship_list.pop(len(ship_list) - 1)

        # Colisión con los aliens
        for bullet in bullets:
            collision_alien = pygame.sprite.spritecollide(bullet, all_aliens, True)
            if collision_alien != []:
                score.new_score()
                for alien in collision_alien:
                    explotion = Explosion(alien.rect.centerx, alien.rect.centery)
                    explotion_img.add(explotion)
                bullet.kill()

            if len(all_aliens) == 0:
                score.new_level()
                speed += constants.SPEED_INCREASE
                create_aliens(speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Actualiza el lienzo para mostrar los cambios
        pygame.display.flip()

        # Pantalla final
        if len(ship_list) == 0:
            bullets.empty()
            alien_bullets_list.empty()
            score.highest_score()
            screen.blit(bg, (0, 0))
            create_texts()

            text_rect = game_over_text.get_rect(center=(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2))
            screen.blit(game_over_text, text_rect)
            # Botón reinicio
            restart_button = restart_img.get_rect()
            # restart_button.center = (constants.SCREEN_WIDTH // 2 - 100, constants.SCREEN_HEIGHT // 2 + 50)
            restart_button.center = (constants.SCREEN_WIDTH // 2 - 100, constants.SCREEN_HEIGHT // 2 + 100)
            screen.blit(restart_img, restart_button)
            # Botón exit
            exit_button = exit_img.get_rect()
            # exit_button.center = (constants.SCREEN_WIDTH // 2 + 100, constants.SCREEN_HEIGHT // 2 + 50)
            exit_button.center = (constants.SCREEN_WIDTH // 2 + 100, constants.SCREEN_HEIGHT // 2 + 100)
            screen.blit(exit_img, exit_button)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    score.score = 0
                    all_aliens.empty()
                    all_aliens = pygame.sprite.Group()
                    explotion_img.empty()
                    explotion_img = pygame.sprite.Group()
                    create_aliens(speed)
                    ship_list = create_ship_list()

                if exit_button.collidepoint(event.pos):
                    run = False


pygame.quit()
