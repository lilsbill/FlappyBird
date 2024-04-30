import pygame
pygame.init()


class about_new():

    def __init__(self):
        self.white = (255, 255, 255)
        self.win_height = 720
        self.win_width = 1200

        #set up screen
        self.SCREEN = pygame.display.set_mode((self.win_width, self.win_height))

    def run_text(self):
        self.SCREEN.fill(self.white)

        pygame.display.set_caption("Check?")


        background_img = pygame.image.load("Menu_images/seaweed.jpeg")

        self.SCREEN.blit(background_img, (0,0))

        pygame.display.update()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                   return  # Exit the loop if 'x' key is pressed

        