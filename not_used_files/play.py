import pygame
pygame.init()




class coral():

    def __init__(self):
        self.white = (255, 255, 255)
        self.win_height = 720
        self.win_width = 1200

        #set up screen
        self.SCREEN = pygame.display.set_mode((self.win_width, self.win_height))

    def run_text(self):
        self.SCREEN.fill(self.white)

        pygame.display.set_caption("Check?")


        background_img = pygame.image.load("Menu_images/new.jpg")

        self.SCREEN.blit(background_img, (0,0))

        play_input = pygame.key.get_pressed()
        if play_input[pygame.K_x]:
            return 2