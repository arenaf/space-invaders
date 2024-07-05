import pygame


class Ship:
    def __init__(self, x, y, image, screen):
        # self.ship_width = 40
        # self.ship_height = 20
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y - self.rect.width)
        self.screen = screen
        # self.position = [x, y - self.ship_height * 2]

    def create_ship(self):
        self.screen.blit(self.image, self.rect)
        # self.new_ship = pygame.Rect((self.position[0], self.position[1], self.ship_width, self.ship_height))
        # return self.new_ship

    def move_right(self):
        if self.rect.x < 760:
            self.rect.x += 5
        # if my_ship.left < 760:
        #     return my_ship.move_ip(self.speed, 0)

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= 5
        # if my_ship.left > 0:
        #     return my_ship.move_ip(-1*self.speed, 0)
