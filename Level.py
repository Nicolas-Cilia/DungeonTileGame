import pygame
import random
from Tile import *
from Enemy import *

class Level(pygame.sprite.Sprite):
    def __init__(self, images, player):
        super(). __init__()

        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.player = player
        self.start_pos = (0, 0)
        self.end_pos = (0, 0)
        self.start = None
        self.end = None

        self.generate_level(images)

    def update(self):
        self.enemies.update()
        self.player.update()

    def draw(self, screen):
        self.floors.draw(screen)
        self.walls.draw(screen)
        self.player.draw(screen)
        self.enemies.draw(screen)




    def place_start(self, level_grid):
        for x in range(len(level_grid)):
            for y in range (1, len(level_grid[0])):
                if level_grid[x][y] == "f":
                    self.start_pos = (x * 32 + 1, y * 32 + 1)
                    level_grid[x][y - 1] = "s"
                    return

    def place_end(self, level_grid):
        for x in range(len(level_grid) - 2, 0, -1):
            for y in range (1, len(level_grid[0])- 1):
                if level_grid[x][y] == "f":
                    self.end_pos = (x * 32, y * 32)
                    level_grid[x][y] = "e"
                    return


    def generate_level(self, images):
        level_grid = []

        screen_info = pygame.display.Info()

        for i in range((screen_info.current_w// 32) + 1):
            level_grid.append(["w"] * ((screen_info.current_h// 32) +1))

        num_floors = int(len(level_grid) * len(level_grid[0]) * 0.6)

        floor_count = 0

        x = len(level_grid) // 2
        y = len(level_grid[0]) // 2

        while floor_count < num_floors:
            if level_grid[x][y] != "f":
                level_grid[x][y] = "f"
                floor_count +=1

            dir = random.randint(1, 4)

            if dir == 1 and x > 2:
                x -= 1
            if dir == 2 and x < len(level_grid) - 4:
                x += 1
            if dir == 3 and y > 2:
                y -= 1
            if dir ==4 and y < len(level_grid[0]) - 4:
                y += 1
        self.place_start(level_grid)
        self.place_end(level_grid)

        for x in range(len(level_grid)):
            for y in range(len(level_grid[0])):
                if level_grid[x][y] == "w":
                    self.walls.add(Tile(images["w"], (x * 32, y * 32)))
                if level_grid[x][y] == "f":
                    self.floors.add(Tile(images["f"], (x * 32, y * 32)))
                if level_grid[x][y] == "s":
                    self.start = Door(images["normal door"], (x * 32, y * 32), True)
                    self.walls.add(self.start)
                if level_grid[x][y] == "e":
                    self.end = Door(images["normal door"], (x * 32, y * 32), False)
                    self.walls.add(self.end)

        for i in range(8):
            self.enemies.add(Enemy("Images/big monster.png", random.choice(self.floors.sprites()).rect.center, self))

# class Intro_Room(Level)
