# menu screen set up
import pygame
pygame.init()


class new_menu():

    def __init__(self):
        #give some basics for the screen setup
        self.white = (255, 255, 255)
        self.blue = (0, 0, 255)
        self.win_height = 720
        self.win_width = 1200

        #set up screen
        self.SCREEN = pygame.display.set_mode((self.win_width, self.win_height))
        pygame.display.set_caption("Main Menu")

        #sets up font   
        self.font = pygame.font.SysFont("arialblack", 40)
        #sets color of text to blue
        self.TEXT_COL = (self.blue)

    #function for the text on the screen
    def draw_text(self, text, font, TEXT_COL, x, y):
        img = font.render(text, True, TEXT_COL)
        self.SCREEN.blit(img, (x, y))

    def run(self):
        run = True
        while run:
            self.SCREEN.fill(self.white)

            self.draw_text("Press SPACE to begin!", self.font, self.TEXT_COL, 250, 250)

            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    run = False
                pygame.display.update()

                user_input = pygame.key.get_pressed()
                if user_input[pygame.K_SPACE]:
                    #main()
                    return 2

                pygame.display.update()
                
        pygame.quit

#def main():
    #pygame.display.set_caption("again?")

#menu = new_menu()
#menu.run()




