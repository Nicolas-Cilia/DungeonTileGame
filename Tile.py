import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super() . __init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos


class Door(Tile):
    def __init__(self, images, pos, unlocked):
        super(). __init__(images[unlocked], pos)
        self.images = images
        self.unlocked = unlocked

    def unlock(self):
        self.unlocked = True
        self.image = pygame.image.load(self.images[self.unlocked])
