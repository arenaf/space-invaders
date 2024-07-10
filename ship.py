import constants


class Ship:
    def __init__(self, x, y, image, screen):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y - self.rect.width)
        self.screen = screen

    def create_ship(self):
        self.screen.blit(self.image, self.rect)

    def move_right(self):
        if self.rect.x < constants.MAX_SCREEN_POSITION:
            self.rect.x += constants.SHIP_MOVEMENT

    def move_left(self):
        if self.rect.x > constants.MIN_SCREEN_POSITION:
            self.rect.x -= constants.SHIP_MOVEMENT
