import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, image, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)
        # self.screen = screen
        self.speed = speed

    def update(self, aliens):
        for alien in aliens:
            if alien.rect.x > 760:
                self.speed *= -1
            if alien.rect.x < 0:
                self.speed *= -1
        self.rect.x += self.speed
