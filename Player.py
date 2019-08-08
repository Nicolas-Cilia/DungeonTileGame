import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super(). __init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect
        self.image = pygame.transform.scale(self.image,(32, 32))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.movement = [0, 0]

    def move_x(self, distance):
        self.movement[0] = distance

    def move_y(self, distance):
        self.movement[1] = distance

    def update(self):
        self.rect.move_ip(self.movement)

        self.movement = [0, 0]

    def draw(self, screen):
        screen.blit(self.image, self.rect)