import pygame
import sys
from pygame.locals import *
from Level import *
from Player import *

pygame.init()

size = (width, height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)

screen = pygame.display.set_mode(size, FULLSCREEN)

clock = pygame.time.Clock()

images = {"w": "Images/brown brick wall.png", "f": "Images/sandstone_wall_0.png",
         "player": {"u": "Images/zelda back.png",
                    "d": "Images/zelda image front.png",
                    "l": "Images/zelda facing left.png",
                    "r": "Images/zelda facing right.png"},
          "normal door": {True:"Images/open_normal_door.png", False: "Images/closed_normal_door.png"}}

player = Player(images["player"], (32, 32))

def main():
    current_level = Level(images, player)
    player.next_level (current_level)
    global screen
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    sys.exit()
                if event.key == K_ESCAPE:
                    screen = pygame.display.set_mode((600, 400))
                if event.key == K_F11:
                    screen = pygame.display.set_mode(size, FULLSCREEN)
                if event.key == K_w:
                    player.move_y(-16)
                if event.key == K_s:
                    player.move_y(16)
                if event.key == K_a:
                    player.move_x(-16)
                if event.key == K_d:
                    player.move_x(16)
                if event.key == K_UP:
                    player.move_y(-16)
                if event.key == K_DOWN:
                    player.move_y(16)
                if event.key == K_LEFT:
                    player.move_x(-16)
                if event.key == K_RIGHT:
                    player.move_x(16)

        screen.fill((0, 0, 0))
        current_level.update()
        current_level.draw(screen)
        player.update()
        player.draw(screen)
        pygame.display.flip()



main()