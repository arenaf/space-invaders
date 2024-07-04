import pygame


class Bullet:
    def __init__(self, x, y):
        self.coord_x = x
        self.coord_y = y
        self.shot_width = 3
        self.shot_height = 5
        self.speed = -4
        self.rect = pygame.Rect((self.coord_x, self.coord_y, self.shot_width, self.shot_height))

    def move_bullet(self):
        self.rect.y += self.speed
