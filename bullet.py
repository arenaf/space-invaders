import pygame
import constants


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.coord_x = x
        self.coord_y = y
        self.shot_width = constants.BULLET_WIDTH
        self.shot_height = constants.BULLET_HEIGHT
        self.speed = constants.BULLET_SPEED
        self.rect = pygame.Rect((self.coord_x, self.coord_y, self.shot_width, self.shot_height))

    def move_bullet(self):
        self.rect.y -= self.speed

    def move_bullet_alien(self):
        self.rect.y += self.speed
