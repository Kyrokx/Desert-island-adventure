import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load("Assets/Player.png")
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.speed = 2
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.images = {
            'down': self.get_image(0, 0),
            'up': self.get_image(0, 96),
            'left': self.get_image(0, 32),
            'right': self.get_image(0, 64)
        }

    def save_location(self): self.old_position = self.position.copy()

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        image.set_colorkey([0, 0, 0])
        return image

    def change_image(self, name):
        self.image = self.images[name]

    def move_up(self):
        self.position[1] -= self.speed

    def move_down(self):
        self.position[1] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_right(self):
        self.position[0] += self.speed
