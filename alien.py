import pygame
import constants


class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, image, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed

    def update(self, aliens):
        for alien in aliens:
            if alien.rect.x > constants.MAX_SCREEN_POSITION:
                self.speed *= -1
            if alien.rect.x < constants.MIN_SCREEN_POSITION:
                self.speed *= -1
        self.rect.x += self.speed
