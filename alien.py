import pygame


class Alien:
    def __init__(self, x, y, image, screen):
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)
        self.screen = screen

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)

    def create_aliens(self, row, col):
        all_aliens = []
        new_y = self.y
        for i in range(row):
            new_x = self.x
            for j in range(col):
                all_aliens.append((new_x, new_y))
                new_x += 60
            new_y += 60
        return all_aliens
