import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos, level):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.level = level
        self.health = 50
        self.damage = 10
        self.defense = 1
        self.attack_delay = 60

        self.movement = pygame.math.Vector2(0, 8)
        self.dir = random.choice([0, 90, 180 ,270])
        self.movement.rotate_ip(self.dir)

    def attack(self, player):
        player.defend(self.damage)

    def defend(self, damage):
        self.health -= (damage - self.defense)
        if self.health <= 0:
            self.kill()
            if len(self.level.enemies) == 0:
                self.level.end.unlock()

    def update(self):
        self.attack_delay -=1
        if pygame.sprite.collide_rect(self, self.level.player):
            if self.attack_delay <=0:
                self.attack(self.level.player)
                self.attack_delay = 60

            return

        self.rect.move_ip(self.movement)
        hits = pygame.sprite.spritecollide(self, self.level.walls, False)
        if len(hits) >= 1:
            self.movement.rotate_ip(180)
            self.rect.move_ip(self.movement)
            self.dir = random.choice([0, 90, 270])
            self.movement.rotate_ip(self.dir)
            self.rect.move_ip(self.movement)