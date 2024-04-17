# menu screen set up
import pygame
pygame.init()

#give some basics for the screen setup
WHITE= (255, 255, 255)
BLUE= (0, 0, 255)
SCREEN_WIDTH=800
SCREEN_HEIGHT=600

#set up screen
SCREEN=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#sets up font 
font = pygame.font.SysFont("arialblack", 40)
#sets color of text to blue
TEXT_COL = (BLUE)

#function for the text on the screen
def draw_text(text, font, TEXT_COL, x, y):
    img= font.render(text, True, TEXT_COL)
    SCREEN.blit(img, (x, y))

run = True
while run:
        SCREEN.fill(WHITE)

        draw_text("Press SPACE to begin!", font, TEXT_COL, 160, 250)

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run= False
        pygame.display.update()
pygame.quit



