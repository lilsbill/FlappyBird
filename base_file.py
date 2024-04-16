#import statement

import pygame, sys
from pygame.locals import *

#initalize, set-up pygame

pygame.init()
clock = pygame.time.Clock()

windowWidth = 1200
windowHeight = 700

windowSurface = pygame.display.set_mode((windowWidth,windowHeight), 0, 32)
pygame.display.set_caption('BEGIN TEST')
background_image = pygame.image.load("images/under_sea.jpeg").convert()
background_image = pygame.transform.scale(background_image, (windowWidth,windowHeight))

ground_image = pygame.image.load("images/sand.png")

scroll_speed = 1

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.x <= -windowWidth:
            self.kill()

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def main():

    x_pos_ground, y_pos_ground = 0, 520
    ground = pygame.sprite.Group()
    ground.add(Ground(x_pos_ground, y_pos_ground))

    running = True
    while running:
        quit_game

        # Blit the background image onto the screen
        windowSurface.blit(background_image, (0, 0))

        ground.draw(windowSurface)

        ground.update()
        clock.tick(60)
        # Update the display
        pygame.display.update()

main()

