import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super() . __init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos