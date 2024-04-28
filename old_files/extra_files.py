BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

basicFont = pygame.font.SysFont(None,48)

text = basicFont.render('Hello World!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

#draw a white bg on the surface of the window

windowSurface.fill(WHITE)

# draw green polygon

pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

#draw some blue lines

pygame.draw.line(windowSurface, BLUE, (60,60), (120,60), 4)
pygame.draw.line(windowSurface, BLUE, (120,60), (60,120), 4)
pygame.draw.line(windowSurface, BLUE, (60,120), (120,120), 4)
pygame.draw.line(windowSurface, BLUE, (60,60), (120,120), 4)

#draw a circle

pygame.draw.circle(windowSurface, BLUE, (300,50), 20, 0)

#draw an ellipse

pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

#draw the text background rectangle onto surface
pygame.draw.rect(windowSurface, RED, (textRect.left-20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

#get pixel array of the sruface

pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

#draw text onto the surface

windowSurface.blit(text, textRect)

#draw the window onto the screen

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
