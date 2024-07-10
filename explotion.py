import pygame
import constants


class Explotion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(f"assets/img/exp{i}.png")
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.cont = 0

    def update(self):
        speed = constants.SPEED_EXPLOTION
        self.cont += 1

        if self.index < len(self.images) - 1 and self.cont >= speed:
            self.cont = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.cont >= speed:
            self.kill()
