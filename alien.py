import pygame


class Alien:
    def __init__(self, x, y, image, screen):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = screen

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)
