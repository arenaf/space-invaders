import pygame


class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.ship_width = 40
        self.ship_height = 20
        self.shot_width = 5
        self.shot_height = 10
        self.speed = 5
        self.position = [x, y - self.ship_height * 2]

    def create_ship(self):
        self.new_ship = pygame.Rect((self.position[0], self.position[1], self.ship_width, self.ship_height))
        return self.new_ship

    def move_right(self, my_ship):
        if my_ship.left < 760:
            return my_ship.move_ip(self.speed, 0)

    def move_left(self, my_ship):
        if my_ship.left > 0:
            return my_ship.move_ip(-1*self.speed, 0)

    def attack(self, my_ship):
        shot = pygame.Rect((my_ship.rect.centerx, my_ship.rect.centery, self.shot_width, self.shot_height))
        return shot




