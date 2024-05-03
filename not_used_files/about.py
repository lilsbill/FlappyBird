import pygame
from pygame.locals import *
pygame.init()
import sys


class about_new():

    def __init__(self):
        self.white = (255, 255, 255)
        self.win_height = 720
        self.win_width = 1200

        #set up screen
        self.SCREEN = pygame.display.set_mode((self.win_width, self.win_height))

    def run_text(self):
        image_filenames = ["Menu_images/Coral.jpeg", "Menu_images/main.jpeg", "Menu_images/seaweed.jpeg"]  # Add more filenames as needed
        images = [pygame.image.load(filename) for filename in image_filenames]

        scroll_y = 0

        running = True
        while running:
            #screen.fill(WHITE)
    
            # Create a surface for scrolling
            scroll_surface = pygame.Surface((self.win_width, len(images) * images[0].get_height()))
            
            # Blit images to the scrolling surface
            y_offset = 0
            for image in images:
                scroll_surface.blit(image, (0, y_offset))
                y_offset += image.get_height()
            
            # Blit the scrolling surface to the screen
            self.SCREEN.blit(scroll_surface, (0, 0 - scroll_y))
            
            # Event handling
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        scroll_y += 10
                    elif event.key == K_DOWN:
                        scroll_y -= 10
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 4:  # Scroll up
                        scroll_y += 50
                    elif event.button == 5:  # Scroll down
                        scroll_y -= 50
            
            # Limit scroll position
            max_scroll_y = scroll_surface.get_height() - self.win_height
            scroll_y = max(min(scroll_y, 0), -max_scroll_y)
            
            # Determine which images are visible on the screen
            first_visible_index = max(abs(scroll_y) // images[0].get_height(), 0)
            last_visible_index = min(first_visible_index + self.win_height // images[0].get_height() + 1, len(images))
            
            # Preload images if needed
            if first_visible_index > 0:
                for i in range(first_visible_index):
                    if i < len(images):
                        scroll_surface.blit(images[i], (0, i * images[0].get_height()))
            
            if last_visible_index < len(images):
                for i in range(last_visible_index, len(images)):
                    scroll_surface.blit(images[i], (0, i * images[0].get_height()))
            
            pygame.display.flip()

        