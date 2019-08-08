import pygame
import sys
from pygame.locals import *
from Level import *
pygame.init()

size = (width, height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)

screen = pygame.display.set_mode(size, FULLSCREEN)

clock = pygame.time.Clock()

images = {"w": "images/wall_1.png", "f": "images/Floor1.png"}

def main():
    current_level = Level(images)
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
        screen.fill((0, 0, 0))
        current_level.update()
        current_level.draw(screen)
        pygame.display.flip()


main()