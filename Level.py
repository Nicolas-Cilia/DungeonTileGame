import pygame
import random
from Tile import *

class Level(pygame.sprite.Sprite):
    def __init__(self, images):
        super(). __init__()

        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()

        self.generate_level(images)


    def draw(self, screen):
        self.floors.draw(screen)
        self.walls.draw(screen)

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

        for x in range(len(level_grid)):
            for y in range(len(level_grid[0])):
                if level_grid[x][y] == "w":
                    self.walls.add(Tile(images["w"], (x * 32, y * 32)))
                if level_grid[x][y] == "f":
                    self.walls.add(Tile(images["f"], (x * 32, y * 32)))
