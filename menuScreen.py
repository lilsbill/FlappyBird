# menu screen set up
import pygame
pygame.init()


#from play import coral

#play = coral()

#from about import about_new

#about = about_new()


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

        self.show_play_screen = False
        self.show_about_screen = False

    def help_menu(self):
        self.SCREEN.fill(self.white)

        coral_img = pygame.image.load("Menu_images/coral.jpeg")

        self.SCREEN.blit(coral_img, (0,0))


    #function for the text on the screen
    def draw_text(self, text, font, TEXT_COL, x, y):
        img = font.render(text, True, TEXT_COL)
        self.SCREEN.blit(img, (x, y))

    def basic(self):
        background_img = pygame.image.load("Menu_images/main.jpeg")
        self.SCREEN.blit(background_img, (0,0))

    def input_menu(self):
        run = True
        while run: 
            self.basic()
            new_input = 0
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return 2
                    elif event.key == pygame.K_x:
                        self.show_play_screen = True
                        self.show_about_screen = False
                    elif event.key == pygame.K_z:
                        self.show_about_screen = True
                        self.show_play_screen = False   
                    
                if self.show_play_screen:
                    new_input = play.run_text()
                elif self.show_about_screen:
                    new_input = about.run_text()

                if new_input == 2:
                    self.show_play_screen = False
                    self.show_about_screen = False
                
                pygame.display.update()
            
        

    def run(self):
        run = True
        while run:
            background_img = pygame.image.load("Menu_images/main.jpeg")
            self.SCREEN.blit(background_img, (0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return 2
                    elif event.key == pygame.K_x:
                        #self.show_play_screen = True
                        #self.show_about_screen = False

                        self.SCREEN.fill(self.white)

                        pygame.display.set_caption("Press V to Return")


                        background_img = pygame.image.load("Menu_images/new.jpg")
                        background_img = pygame.transform.scale(background_img,(1200, 700))

                        self.SCREEN.blit(background_img, (0,0))

                        pygame.display.update()

                        running = True
                        while running:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                                    background_img = pygame.image.load("Menu_images/main.jpeg")
                                    self.SCREEN.blit(background_img, (0,0))
                                    return  # Exit the loop if 'x' key is pressed

                    elif event.key == pygame.K_z:
                        #about.run_text()
                        self.SCREEN.fill(self.white)

                        pygame.display.set_caption("Press V to Return")


                        background_img = pygame.image.load("Menu_images/about2.png")
                        background_img = pygame.transform.scale(background_img,(1200, 700))

                        self.SCREEN.blit(background_img, (0,0))

                        pygame.display.update()

                        running = True
                        while running:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                                    background_img = pygame.image.load("Menu_images/main.jpeg")
                                    self.SCREEN.blit(background_img, (0,0))

                    elif event.key == pygame.K_y:
                        self.SCREEN.fill(self.white)

                        pygame.display.set_caption("Check?")


                        background_img = pygame.image.load("Menu_images/seaweed.jpeg")

                        self.SCREEN.blit(background_img, (0,0))

                        pygame.display.update()



                        running = True
                        while running:
                            for event in pygame.event.get():
                                #if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                                #    background_img = pygame.image.load("Menu_images/seaweed.jpeg")
                                #    self.SCREEN.blit(background_img, (0,0))
                                #    break
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                                    background_img = pygame.image.load("Menu_images/main.jpeg")
                                    self.SCREEN.blit(background_img, (0,0))
                                    return  # Exit the loop if 'x' key is pressed


                elif event.type == pygame.KEYUP:
                    pass  # You can handle key releases here if needed

            new_input = 0

            if self.show_play_screen:
                new_input = play.run_text()
            elif self.show_about_screen:
                new_input = about.run_text()

            if new_input == 2:
                self.show_play_screen = False
                self.show_about_screen = False


            pygame.display.update()   
                
        pygame.quit

#def main():
    #pygame.display.set_caption("again?")

#menu = new_menu()
#menu.run()




