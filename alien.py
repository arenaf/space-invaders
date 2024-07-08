import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, image, screen):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)
        self.screen = screen
        self.speed = 1

    # def draw_alien(self):
    #     self.screen.blit(self.image, self.rect)

    def create_aliens(self, row, col):
        all_aliens = []
        new_y = self.y
        for i in range(row):
            new_x = self.x
            for j in range(col):
                all_aliens.append((new_x, new_y))
                new_x += 50
            new_y += 50
        return all_aliens

    # def move_alien(self):
    #     if self.rect.x < 760:
    #         self.rect.x += self.speed
    #
    # def move(self, movement):
    #     if movement:
    #         self.rect.x += self.speed
    #         # print("True ",  movement)
    #     if movement == False:
    #         self.rect.x -= self.speed
    #         # print("False ", movement)
    #
    # def move_right(self):
    #     print(self.rect.x)
    #     self.rect.x += self.speed
    #
    # def move_left(self):
    #     self.rect.x -= self.speed

    def update(self, aliens):
        for alien in aliens:
            if alien.rect.x > 760:
                self.speed *= -1
            if alien.rect.x < 0:
                self.speed *= -1
        self.rect.x += self.speed
