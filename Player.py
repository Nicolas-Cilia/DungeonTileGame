import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, images, pos):
        super(). __init__()
        self.images = images
        self.image = pygame.image.load(images["d"])
        self.rect = self.image.get_rect
        self.image = pygame.transform.smoothscale(self.image,(30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.movement = [0, 0]
        self.dir = "d"
        self.level = None
        self.health = 100
        self.alive = True

    def defend(self, damage):
        self.health -= damage
        if self.health <=0:
            self.alive = False



    def next_level(self, level):
        self.level = level
        self.movement = [0,0]
        self.rect.topleft = level.start_pos


    def move_x(self, distance):
        self.movement[0] = distance
        if distance > 0:
            self.dir = "r"
        else:
            self.dir = "l"


    def move_y(self, distance):
        self.movement[1] = distance
        if distance > 0:
            self.dir = "d"
        else:
            self.dir = "u"

    def update(self):
        self.image = pygame.image.load(self.images[self.dir])
        self.rect.move_ip(self.movement)
        self.image = pygame.transform.smoothscale(self.image, (30, 30))

        hits = pygame.sprite.spritecollide(self, self.level.walls, False)
        if len(hits) >=1:
            if pygame.sprite.collide_rect(self, self.level.end) and self.level.end.unlocked:
                return 1
            self.movement[0] *= -1
            self.movement[1] *= -1
            self.rect.move_ip(self.movement)

        self.movement = [0, 0]

    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, self.rect)